# learning eBPF

- 准备环境

   创建虚拟机

   ```shell
   cd vm-setup
   ssh-keygen -t rsa -C ubuntu -f multipass-key
   vi cloud-init.yaml
   multipass launch --name vmx --cpus 2 --memory 2G --disk 5G --cloud-init cloud-init.yaml
   ```

   安装开发工具

   ```shell
   # For Ubuntu20.10+
   sudo apt-get install -y  make clang llvm libelf-dev libbpf-dev bpfcc-tools libbpfcc-dev linux-tools-$(uname -r)    linux-headers-$(uname -r)

   # For RHEL8.2+
   sudo yum install libbpf-devel make clang llvm elfutils-libelf-devel bpftool bcc-tools bcc-devel
   ```

- 编写 eBPF 模块

   [代码](./01/hello.c)

- 使用 BCC 库开发一个用户态程序

   [代码](./01/hello.py)

- 执行
   
   ```shell
   python3 hello.py
   ```
