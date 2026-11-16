from collections import defaultdict, deque


class SlidingWindowRateLimiter:
    def __init__(self, limit: int, window_seconds: int):
        if limit < 1 or window_seconds < 1:
            raise ValueError("Limit and window must be positive")
        self._limit = limit
        self._window_seconds = window_seconds
        self._accepted: dict[str, deque[int]] = defaultdict(deque)
        self._last_timestamp: int | None = None

    def allow(self, tenant: str, timestamp: int) -> bool:
        if self._last_timestamp is not None and timestamp < self._last_timestamp:
            raise ValueError("Timestamps must be nondecreasing")
        self._last_timestamp = timestamp

        requests = self._accepted[tenant]
        cutoff = timestamp - self._window_seconds
        while requests and requests[0] <= cutoff:
            requests.popleft()

        if len(requests) >= self._limit:
            return False
        requests.append(timestamp)
        return True


if __name__ == "__main__":
    limiter = SlidingWindowRateLimiter(limit=2, window_seconds=10)
    requests = [("acme", 0), ("acme", 4), ("acme", 9), ("beta", 9), ("acme", 10)]

    for tenant, timestamp in requests:
        status = "ALLOW" if limiter.allow(tenant, timestamp) else "REJECT"
        print(f"{tenant} at {timestamp}s -> {status}")
