import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    try:
    # note: .*? will match zero or more characters, but because of the ? it will try to match as few characters as possible.
    # note: s? means the s may or may not appear
    # note: (?:www\.)? - non-capturing so what's in () won't be sent back and the ? means that what's in this may or may not appear
    # note: [^] - complementing the set, the ^ here means basically not like [^abcdef] would be not any of those letters but everything else is okay.

        pattern = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([^"/]+)".*?</iframe>'

        match = re.search(pattern, s, re.IGNORECASE)

        if match:
            video_id = match.group(1)
            return f"https://youtu.be/{video_id}"
        else:
            return None
    except Exception:
        return None

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/watch
