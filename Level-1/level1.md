# 用法

---

1. 克隆仓库
   `git clone https://github.com/SISUBEN/cyber-security-educate.git`
2. 打开cyber-security-educate > *Level-1* > application

   `cd cyber-security-educate/Level-1/applicaltion `
3. 安装模块

   `pip install -r requirements.txt`
4. 启动app

   `flask run`

# 注意

---

- 此程序必须部署在局域网内
- > Example: *(局域网192.168.0.0/24)*
  >
- > - Server: 192.168.0.23
  >   - 在此电脑运行 `python server.py`
  >   - 注：必须先运行server.py再运行client.py或contorl.py，不然会导致客户端找不到服务端
  > - Client1:192.168.0.24
  >   - 在此电脑运行 `python client.py`
  > - Client2:192.168.0.25
  >   - 在此电脑运行 `python client.py`
  > - Client3:192.168.0.26
  >   - 在此电脑运行 `python client.py`
  > - Contorl:192.168.0.27
  >   - 在此电脑运行 `python contorl.py`
  >


# 效果

---

![image-20221030222125605](https://github.com/SISUBEN/cyber-security-educate/blob/main/Level-1/image/image-20221030222125605.png)

![image-20221030222407352](https://github.com/SISUBEN/cyber-security-educate/blob/main/Level-1/image/image-20221030222407352.png)

![image-20221030222451387](https://github.com/SISUBEN/cyber-security-educate/blob/main/Level-1/image/image-20221030222451387.png)
