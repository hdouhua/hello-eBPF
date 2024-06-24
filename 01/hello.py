#!/usr/bin/env python3

# 1) import bcc library
from bcc import BPF


def main():
    # 2) load BPF program
    b = BPF(src_file="hello.c")

    # 3) attach kprobe（内核探针）
    b.attach_kprobe(event="do_sys_openat2", fn_name="hello_world")

    # 4) read and print /sys/kernel/debug/tracing/trace_pipe - 这是内核调试文件
    try:
        b.trace_print()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
