def deco(color_type: str):
    ANSI_COLORS = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "magenta": "\033[95m",
        "reset": "\033[0m"
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            color = ANSI_COLORS.get(color_type, ANSI_COLORS["reset"])
            result = func(*args, **kwargs)
            return f"{color}{result}{ANSI_COLORS['reset']}"
        return wrapper

    return decorator
