from collections import defaultdict
import time
from typing import Dict


class SimpleRateLimiter:
    """Simple in-memory per-identifier rate limiter.

    NOTE: Only suitable for single-process demo/dev. Use Redis or a distributed rate-limiter for production.
    """

    def __init__(self, max_tokens_per_minute: int = 10000):
        self.max_tokens_per_minute = max_tokens_per_minute
        self.usage: Dict[str, int] = defaultdict(int)
        self.window_start: Dict[str, float] = defaultdict(lambda: time.time())

    def allow(self, user_id: str, tokens: int = 0) -> bool:
        now = time.time()
        if now - self.window_start[user_id] > 60:
            # reset
            self.usage[user_id] = 0
            self.window_start[user_id] = now
        if self.usage[user_id] + tokens > self.max_tokens_per_minute:
            return False
        self.usage[user_id] += tokens
        return True

    def reset(self, user_id: str) -> None:
        self.usage[user_id] = 0
        self.window_start[user_id] = time.time()


rate_limiter = SimpleRateLimiter()
