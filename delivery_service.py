def min_platforms(robots: list[int], limit: int) -> int:
    robots.sort()
    left, right = 0, len(robots) - 1
    platforms = 0

    while left <= right:
        if robots[left] + robots[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms


if __name__ == "__main__":
    robots = list(map(int, input().split()))
    limit = int(input())
    print(min_platforms(robots, limit))
