# imuke
基于selenium的智慧树自动刷课软件

python写的，基于selenium，默认打开chrome，也可以更换其他浏览器。
<b>自动登录需要设置账号密码</b>，不放心的同学可以不填或者进入自定义设置切换到手动登录模式。
基本上只要智慧树没有太大的更新这个程序可以一直用。

# 

关于驱动：

如果程序提示<b>'加载驱动失败'</b>，那就说明你的chrome浏览器或者其他浏览器的chrome内核版本和我的预置版本不一致了，不过这都是小问题，解决办法是到 'http://npm.taobao.org/mirrors/chromedriver/' 这个网站或其他可以下载驱动的网站下载一个对应你浏览器的chromedriver。
至于<b>怎么样才能知道自己浏览器版本对应的驱动</b>，我准备了张挺旧图片，但我感觉别的都不太准，可能是我还用不熟吧，大概就是3个版本升一次驱动版本的样子，驱动也就6MB，看不明白多试几个就行了。
![版本](https://user-images.githubusercontent.com/33678058/46445414-63a5a280-c7a9-11e8-9b0d-a6183444b2f7.png)，
