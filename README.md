 ![Logo](Resources/img/Logo_light.png#pic_center)
 # 月時計 \~LunarDial\~
 月時計 \~LunarDial\~ 日历软件
 
 本程序为北京航空航天大学21级致真书院大学计算机基础课程大作业第四题。
 
 <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src='//music.163.com/outchain/player?type=2&id=29164551&auto=1&height=66'></iframe>

## :straight_ruler: 基本要求
> 1. 能够显示当前日期与时间(年月日时分秒),与系统时间或网络时间自动同步、自动更新。
> 2. 具有一般日历的 GUI 界面与功能(可参考电脑、手机中的日历,例子如下图):
> - 特殊显示“当天”,当前时间所在的天在日历中高亮显示;
> - 可以切换显示年份与月份,默认显示本月的日历,但可以任意切换到其他年与月份;
> - 一键“回到今天”,在浏览其他月份时,可以一键回到当前日期所在的月份;
> - 点选某一天可以显示与“今天”相隔的天数;
> - 必做只要求显示公历,以及显示公历节日,例如元旦、劳动节、六一儿童节等,不要求显示阴历日期,及阴历节假日.
> 3. 备忘录/提醒功能:可以添加具有标题、内容、提醒时间(精确到分)等要素的提醒;
可以存储、浏览自己设下的提醒(下一次打开该日历时仍可看到上一次设下的提醒,且提醒仍会于所定时刻生效);可以删除自己设下的提醒;实现类似闹钟的效果,到设定的提醒时间时,进行一定程度的强提醒,强提醒形式可以选择弹窗提示或者加上声音,可自由选择,强提醒结束后此条提醒自动删除。
## :triangular_ruler: 选做内容
> 1. 增加阴历日期显示,阴历节日的显示,例如春节、元宵节、端午节等。
> 2. 备忘录/提醒中加入语音输入系统,可以通过语音输入来设置一条提醒,提醒的标
> 题、内容及提醒时间由语音分析自动填入。
> 3. 增加天气模块,显示选定地点今日的天气。
> 4. 增加日历界面中每个日期的双击事件,弹出窗口中显示当天的存在的提醒,亦可在窗口添加当天的提醒或者进行删除操作。
> 5. 对于时间的显示,可以模拟 LCD 式电子时钟或传统时钟指针式表盘。
> 6. 打包为.exe 可执行文件,添加合适的 icon。

##  :house_with_garden:  运行环境
本程序由Python 3.10编写,暂未测试其它版本Python兼容性。

采用了下列Libraries:

 - PySide6
 - PySqlite3
 - Qt-Material
 - Time
 - Lunar-Python
 - PyInstaller(打包用)
 
由于采用了PySide6,与PyQt5不兼容,因此与自带PyQt5的Anaconda环境不兼容,运行源码前需要将Conda环境卸载干净。

程序需要的字体位于Font目录,需要在运行前安装,由于有部分字体不允许商用,请运行完本程序及时删除。

##  :collision:  运行
不会有人不知道怎么Clone吧,不会吧?

## :art: 自定义
 - /Resources/qss目录放置了全部的StyleSheet,可以根据需要修改。
 - /Resources/alarm.wav为提醒铃声,可以根据需要修改。

## © 著作权
 - 本程序代码部分由KohakuCao本人编写,采用AGPLv3.0协议。
 - 软件名“月時計”源自东方Project,其著作权归ZUN与上海アリス幻樂団所有。
 - 背景图自[https://www.pixiv.net/artworks/72443860](https://www.pixiv.net/artworks/72443860)
 - 默认铃声为《無意識に駆ける》,参见:[https://www.bilibili.com/video/BV1Du411i7K9](https://www.bilibili.com/video/BV1Du411i7K9)