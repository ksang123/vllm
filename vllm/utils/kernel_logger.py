from collections import defaultdict

KERNEL_LOG = defaultdict(int)
ENABLE_KERNEL_LOGGING = True


def log_kernel(name, shape):
    if not ENABLE_KERNEL_LOGGING:
        return
    KERNEL_LOG[(name, tuple(int(x) for x in shape))] += 1

def dump_kernel_log():
    print("=== KERNEL SIZE SUMMARY ===")
    if not KERNEL_LOG:
        print("(empty)")
    for (name, shape), count in sorted(KERNEL_LOG.items()):
        print(f"{name:20s} shape={shape} count={count}")
    print("===========================")