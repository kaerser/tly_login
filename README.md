# TLY-checkin

通过 github action 来实现自动签到（每天签到可以延时一天）。

[TLY 官网](https://tly.com/)。

如果还没有注册的话，可以去[这里](https://tly.la/359834)注册。

具体实现机制：通过登录网站点击签到获取到签到需要的验证码，将验证码发送至百度云文字识别接口识别验证码，再输入签到接口实现自动签到。

## 步骤

### 1 注册并准备百度 AI 开发平台
参考链接：[https://www.jianshu.com/p/3ad636fdab4b](https://www.jianshu.com/p/3ad636fdab4b)

### 2 fork 这个仓库

点击右上角的 fork。

### 3 设置 Github Action 变量

在 fork 后**自己的**仓库中依次点击 `Settings` - `Secrets` - `New repository secret`，依次添加以下变量：
>- `SERVE`
>- `SCKEY`
>- `EMAIL`
>- `PASSWD`
>- `APIKEY`
>- `SECRETKEY`

`SERVE`、 `SCKEY` 为Server酱需要的变量；
`EMAIL`、`PASSWD` 为TLY账号登录的邮箱和密码；
`APIKEY`、`SECRETKEY` 为百度OCR应用的API Key和Secret Key

### 4 运行 

随便发起一个 push 请求，可以修改一下 `README.md`，或者自己给自己点个 star，就可以开始。之后就会每隔 6 小时进行一次签到（因为有时候签到会失败，好像是服务器不太好，就设置一下每小时签到一次保证成功吧）。

注意，在官方文档中有这么一段：

> To prevent unnecessary workflow runs, scheduled workflows may be disabled automatically. When a public repository is forked, scheduled workflows are disabled by default. In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days.

也就是说，**定时执行的任务需要每隔 60 天激活一次**。

## Server酱

参考：[http://sc.ftqq.com/3.version](http://sc.ftqq.com/3.version)
