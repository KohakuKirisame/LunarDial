# 冰雪聪明！
# -------------------------------------------------------
# @By:Kohaku Cao
# @Time:2022-06-26 20:39
# @QQ:1848790911
# @Mail:kohaku@hepnovel.com
# @File:HomeController.py
# @For:月時計 ~Lunar Dial~
# -------------------------------------------------------
# Image From: https://www.pixiv.net/artworks/98484254
#                                                                      rJOqq00QLQQCJUn
#                                                                     UX{QnnQmUCQQQQQQLQLU
#                                                                     QQ              UCQQQQL                      QXzzQ
#                                                                     nQ         {U       QQQJJ            XUJJJQLQLQJCQQJz
#                                                                     z0         zx)jvvvU    CCCJ     UYYJUYJUCJCCQ     nUC
#                                                                     JO         cc/? nvj|rJm  UJYzXYczXXz{              OQ
#                                                                CLCCUjJ)         +)|\|(){|({{{{)jruunn    /f/vn-        ZU
#                                                              {OQQCQX>tJ     +[{){[_!I;i+--+]]-!l>+-}]]\/(\\}}\f/      QO
#                                                               OZ    ~<zYf!}()}?l  rcXzccvz$      `;<?(xf)fn       cJ
#                                                                0OQ   +>zx\)+"  Ynxxxn   n}l<             ^>1jX       XX
#                                                                 OOZQ{i}f{!   rrxn    }-{/(i!               'l]fvC 
#                                                                   Q0U\)!   fjrt   n|){+                   _f{ ^+)nx)}C0QQ
#                                                                    Y|>   n\\/    )||n {n               il   }\n {)/f$  OQ
#                                                        QUxjf\(unzfj),  fjnr    $)({  jj-    |<         ?)    \fn uttjtLQ
#                                                       Qx}[[||rnt{{! \cvnjf    $}] n){(|   ntj  l       pj     jr cYr/)c
#                                                       n}nCCLYr][j /vnf1ru     +]|{)(\   Ux|{t ->       {u]     rn;Xzvlf
#                                                      U))CJUYv    (rf(+{x     -< ){x  Qffft-/-1{       }v(f   -?1{ xv]_v
#                                                     vf}         ?/f\|[t   I  }<jxj|]}]]|jv{11\      ccxn1r   xx<? _i)XQ
#                                                   nCu)    Xxjff()rjff\ i;?>  |<UvCvjnvjrzf\(|\\(\txucjv{)u UUc( / i[{a
#                                                   Ynz/  C\/nnjf Xur   tj-]$  |1xwm   jX/uv-+?[]?//t/fx\(jrvzvn -t `x?n
#                                                   njcnr ujvcuj\ccc   ufu}|   +}(Q0LQp0z ,o      |)XUzvrUzCOzrft{f IY}f
#              nnUXrvYYYvvLJcUX$                    cUUYzcu|x\tcxvt   vnnC//  ?`}fCYcLQ         i  XZJm0YvuXJj(})f  (v}/
#              rCUXcXJJUzvYUcXn|/ttrxuvvcXUJQm        vUcUrtcccz/f   fv}uU|)n (t {Xi             i /xxu/|fj??/nr]f
#               zJJ              '":Ili>+_?}1\XQ       CYu nxjj ffxz fx)xcf)|rnfm +()r"   cXz{n\Q      {_LYnn[)]]}cnf(?n
#                nJCY                         !uQ      nYJCQYJUCcrtcXXnrjxcj/fuxj  +/t{Q  nXv/jxu     XYLLXv\(n  ]xxt?xYYp$
#                  JCCC                        `/Cn      ncQCQC(urcuYc//jxvcr/|x  $[)}jJQQd#  )|t|jjvYcYX/nUQ |c?}?))t_+-[}))\/juc\
#                   \JCCU                        ]JX           tcrzYJuj\zvcc\rr1{\t\)/^"lcCCOLXXYuncufr\jnQ rx/jlf-/        ^:!l]Jr
#                     cCUUc                       !vJ                zXuXXnYzJn"I]]?{XXc{Ynxnc YYvvzz[ncX  f[[?}/\rf           `xU
#                       \YJJUX                     :fU                    dmnuu/U      YcXY/frc     YcX nvt\}_   $             (U
#                          UJCJUn                   "tY             Cccxjjf{i<OxfuY   bv{v}\fuzvCnnxtucYUYfl!!                UU
#                            {JJJJUX                  cc       \u|(/cn([}}1      )|ffzj\Y0jt\xYr}}+tr)]}]-f(l^              \JU
#                               nUJJJUX                xu      Yni-1{?{[_?}|jv{    |f|l<)zCuCc/|>]j zCQO   ?\l;<           vYY
#                                   JCJUJYUUYJJJJJYJYYXcUX     JU         l!-]_-    cX$ :]{vccnn ^-jZ QQQ~v-!;         zYX
#                                      YCnXnnQQQQQ\XJYYCL\    nxr         ?{/ !+})   uXU  -xn/fvcZ >(Y Q0LcY ?/{[++zUzXzccXX
#                                                             Jr}x         n/t {_{f   fvJ }trr}cxYU ^]un Jczz j)i-1jzJzXvzn
#                                                             cx;jv          ff\~:?j$  (Y>/|vX1\n/zcU)cn  nYYX zv( Ii\Y
#                                     $                       Q\ Y/)          j\+  _rp  Jru{unxt\Xnj/M      rj  vn   ?QnJXtnzYC0Jb$
#                                OYcnr/trcYCa                 X? n(            z)}f _v   jt\z c}|jZjun       /u      \UzCYi<+-]}]}1(\/jxvYQ$
#                           zXcxf([_!, :>+]{(trnzQ$           Yi                 fxz;1n{  ?/U Xf\crYz|        r?    'u};           ,l><+?[1{nnl
#                      XUUUYUt?>"            ,!+-}(/jvUk    {C(                jfXx1?_jf  <)tcjX!j/un         f)+rvx<Y<:                   ~XY
#                 UJCCJJUYYn                       :i_[)nnc vJ~l`      {\{ [)\fxtu|[\tztr   !()uj+?<           t-juz.?Xj!"               l1UL
#            tXYYYJUJUn                               fxcvc {YCr({}fjjt|?+<?|/{   Unnxf+f   -;l                f+   $ "\Y)I!$           JYJ
#          JUYYUzn                                 UYYYXv       Qn:(\n   ?{f   {uc/jzun!\v                Qrf  \{l zYcc(njll          YJUv
#          JJJCJU                              CJUUYYY          Q(       nLJJUYvnvxrjc< xr               t)]) ([v)Y-l::l          UCU
#            nCJCCJJJX                     YJJJJJCX             J{;UUn   U/[}1{[lvv|frQLv               r{>l/\[jc[l".\O'I,         QCJn
#                LUUUYXXzzzcvXnnn      nXUJUJJU                 YtrJJJYYC|;      XzjJUJ0CQJf{)|){-<l)[ Ij/nnuttrvU{nXIfUv}/zcYvxvv\)X
#                     nJXYczzYXXYXYXUUcvUUU                           XzQ/        LQYUfcQQQJf(tfjjfncznrjtjYJJJXcYUj\vjQuuYYXYnnnn}
#                                nnzzQz                             $&opOp<        CJCt})|\rcXCQCCLQLQ|<_1))/()/\|f(|n{0+xUc
#                                                  /fCz   nQ/\||/xO^                "l+])|\\//|[??~: nQJCCnxCOQUUOQp
#                                         apCcuxjf/|(1[?+!l^)U    J0'   ;:pf                                   JLCJQCfUvjv\/rcvC
#                                     Ou/\(){}]-<!:        YUi    YQ"   <l{Q)*wMk$$$$$OZmZCYQLYJQqmQkkdZZCQkpQJ/~l^!fJCr_IU+iv-<+_i1YQ
#                                   QJ/i"                  Yu     fQ:    ><JCUYnxxrxj/uvtf)(////|/ffffft\/t/ttft\|\//un(  CxI       !fCQ
#                                  Qv]                    YY      <0>    -fvf}>>>>>l:!-~l  "                ":li>++-!uj{J!uL:l       .-vQ
#                                \Ut!                    XUn       Cr <:i(j}i;      >?|>                              Y)+nxC~l         "|CC
#                               YUX                     cYv       !I)f)~         ~/1                                u{ nx{\t{ill      +zQ
#                             nUJX                     XUc    \|c]nf_          "}j                                 vcj >/-ifu:"    p$>>nJ\
#                            cJJ                     -cYn   Qzf)_;"|zYr            ~xr                                  ncn ;xr)Y?cJUUUJYJYxY{
#                           XJY                  nYczUc     Qz<,+{fcv              rY                                    [z  ^n00CJUzn$
#                          uJc            UYXUYYYXYcXC      QOJrzzzt              nYj                                     |X  .nZ{
#                         {JXUczcXJzzzzzXzXYYUXzn                       Xz                                      "cU   tmz
#                         {XcYcXcYUXczcXvn           \_i zXc                xY-                                       <Jn   (wL
#                                                 COUcr(_"l>{zzn                 XX                                         |Q  { )qQ
#                                              |>  l+1cjv                  \Yr                                         `YY  < {wC
#                                           <   ~{/uYv                    cX                                           +Q<  I {wC
#                                         pQzt?^    \tfcJ                       zz                                            jC    .(mY
#                                      O0Xt],    nzvuc$                         zv                                            ,UX   ^ xZ
#                                   QOCn}I     fucx|                           rc                                              [C    ^ rL
#                                (!      jccux                             (j                                              `vc    `.rQ
#                             bOYn)+.      nccvc                              vX{                                              '+n      'rQ
#                         wQJzr1<'       fux(t               +->;            0U)                    {                          ``_-      'fO
#                     Z0Lzr)_,  <_+++l (xuX_~              +__++!           QO]~                   -_+l                         "`^       'jm
#                 nO0ux\+,  !+__+++++<xucn _~            __-_  _+         JQQ ++                 __-i_+                         ^!"       `^vZ
#              Q0OQc)>. ;__--++i  ~+jvcv  __           -_-+   >_l        JQL :_i               ~-_+  __                      ++_ l_        `,YJO
#            CQQc)]-!~?--_+n     !]ncu   >_>         ___+     +-        UQL  +_              n_-_     __                    __++l'|-       ".+czZ
#         QQJc)!!~-_-+-{        1txz     __       {+__-       +_       LQX   __             _--l      __                  ~__  ~_`~j        ^ )fnZQ
#       QLc/<,>+---            ccc       __     +---+         __      CQJ    +_           +__+         _+                +__    _<.cf        ^ jt?ZZ
#    QQzj[" ^-_              nccn       +_+   ~_--i           -~     LQc     __          _--           +_               +__      _l[c    I    `"n|:Yqn
#  QY)1>                   nvvv         +_  ----             >_i    JQn      -+        <__+             _~             __?        +!Yx  +~~    ;+X/ /w0
# Ct+                     nnu{         >-]?___               +_    XQz      >_?       ___               __            _--         -+\Y __-++   ?--Q  _Ow
# QYXYcccun             vuuf           _+_-+                 _+   \QJ       +_      ---l                >_+          _-l           :~v?_< <+~  {_`ft! "nwO
#  QLLCXvvccXX          uccQQQ         +_]                   -_   LC        +_    ?__+                   _+         _+              'c(~   +_~  -I }Ym  {0O
#    CQOOk jXYYYXc       zJUJJCYnv                           _+  XC         _+   ___                     +_       <__                /v     ~_i __  /0n  ]00
#      nQmmZ  XXXYYYv     -vY nvjnvvcc                      +- --zJ         -~ __-+                      -_<     -__                '<m      +_ -_ ^ vZ  +:JL{
#         mmmOU   XYXYzr ,;+(nLQ  ]xccvjjQ                  ___<vC          _+--+                         _+    >_+                 '^Zv      _+_-  " CO -l.uCU
#           CZQvX    zcvcXt<l>zQQY    nxuvuun              l-_+YC          l-__                           +_   -_+                  l.LQ      ~_+_   `.ZZ~[` )JC
#          Q0CJYXXXr    vcXYu{!ljQQU     {xuzXcn           <-+QJn          ++<                            +_  <_+                    .xO       __+    ^'q/" " ~JC
#        zQQX    1|jxcj    {uYXj]i]vCJY      YXzccn          CYY                                          -- +__                     '}0       i__     `^mL   .,CQ
#       JOJvucvn  --\zzzvj     CUc/]+(cCLY      zzzzz        rJzfxzzzt                                    ~___+                      '}Q        _+      ':wQ   '.JQ
#       QCLQQUzcczYLQ  YzzYJc     QUv/}]\zL0Y     nXXXzv      QLcfvUUXXczXzXYYn                            __+                        ]Y         ~       'i0x   `.CL
#           ZmQCCUzccccvnnYJJUYzn    OJu/){\XJCU     ccnjrn    <fQCY   ccYXXYzzccuvxcYz                    !                 UYJJCJJJztJ                   >YY   `"Lv
#              zCZmm0LYvnuuvucXYYYXu     Qrfxf(xYXn$  |Yrxruvvv!,!fUCUz\       \jnnXzCCCCCQCLQJQCYUCrcUUQJ0mwmULUJUCJJJCCCJLQCJJJYYcv)xC       nLJJUJUJCUCQcLQ/    [UY
#                  QmOZOOQJYvvuccYYYYUYu- uuUzxjfjXXUYzU"II>?)jLJu)-_(uYYYc       XL   -YCQQCYCQL0QCcUOO0JYUUJUCJCJCCCLQQLQnfj/(\{<:^"  QQLLCCCJCUUYUzYQUJcLCU    jltmc
#                       CCJUULL0CJYYYUUYvxx      >vzcxxll` l:;II>/ucvx/)YCCJUU    UU;l!llI;^~c "":I::;",^  <Un    /{?~>~i-(nCm0Q0QCLCUn     JJutu/!  QQ0Q00QLwv
#                            -QZOOOO0QQLz|         vX['">Uci    I/},;>])fcUCCJCUjuQ!l     /xvX!lI":l!;!ill YYr{)ff(){{}[}|\jvUQmZZZQQQLQ     QQLUxzcr)+~I?fYCLQ00Q0p
#                                   Z0ZZ0Q0OQCJjiYYCY QCUUY     zz   I^",:I>_{jXYUfI< nYzYjx)!l  zv     !;!]|\x\(1}}{()xYYccck        (->i>-\uJCCYUQ00C
#                                        pQZQ00LYUj nYYYn      zY             '"n{;!  UYXnfc\   YJc     lI!I^!z+:II;:?{tUY rrj|?tcuvnxj/(}?~~_]{/xcYztXx|/nCL
#                                            )0QUc (CJJCU     XYcCUUUJCUYUUCUZW jc    UX cJJ   UJU            YY     QLU YU/xcuxuccf\tt|||nXXYYYzXXzXnUt)nQCOC
#                                            rQQJYXYYvnccYzUzXYczXccvcXx\xcz)vXYUY    nUtJX   jYfcXzXCYYzYuvrf/u      |Jz UJ XzZcnnxYzczvc0L0LQQQQ000O0ZZ0OZZX
#                                               nUXXCJvvjucvczcnnvcnxr), (vxjccczvnvcXvUXzvzccvzzczzz_!il{uuxjrxxrrcvncXvuuXt 
#                                                   UQ0CQL[^",,;;;:,"''~0c <juYXzcvzUXXJYXXYXzunfxu\?l   ;;l!!!?vx\xxruvUYUvcwZ0ZOOOOZZZOZZwCU
#                                                    QZZQ             ?CLJLUYXUYUzXU0YnncJCLL0XnvL\ `,      :: -YxXQcYYcYC
#                                                  UZmO             .jmYYmCCCLOCwQLCCQ         QZU            iXYXC0JQqCXU
#                                                 OmQ              :JpC                       CmU           ^^zJ
#                                                YqC              +mw<                       JZJ           ;.u0]
#                                                q0             .|pZ                         OQ            '?ZJ
#                                               Yqu           ''nZQ                         +wL           "^O0
#                                               0Z            :J0-                           Z0           .rm-
#                                               mQ           >Om                             0L          ""mY
#                                              zmj         .+Z0                              Q0         i`z0
#                                              0O          _m0                               XZi        ""qJ
#                                              00         >wQ                                ]qC        `\mi
#                                              0Q        ,OZ                                  wm       ^'OO
#                                              On        nq                                   Lm|      ,"wL
#                                             nO|       _Zr                                    wL      '!qz
#                                             c0       <UQ                                     JO      '_p\
#                                             cO       QQ                                      C0      `{w
#                                             UO      }Qr                                      CO      .\m
#                                             cY)---+~xOcf                                     XOYUf{-_l{Oc
#                                           nzrnxfff/\u}\X                                    YU{zUnf///f|xv
#                                          YJY  OO   )Jr                                  CJcJJC     p]<Uc
#                                          YJuff|\/|\|)CzYn                                  JJXx}tcccvu/jYzn
#                                           Lv>-)t||/tvL)                                      O)  ~??-~ +vJp$
#                                          LCUQCLCQQJUjcZ                                     YmxCQb    mQf/uX0o
#                                         U0rZZ00Zm0CQUnqn                                    mX_uXXzzY0OcmrI!1jYmpZk
#                                         qUZQQZZOOmOZQZmZ                                    q|?   -fuJcXQUmmQn||UpQXJ0mpqd
#                                        vZ}JC00vxQ0CCCL_0m                                  UZ]+            nJOpQJU>I~])/Cwp
#                                        ZC+             ,qm{                                CCtczYYUXYJzcYUJC$          ,;cw)
#                                        0L1uYCLpCzzJYLCc+cbX                                 (zJJYYYYYccJUUUYvYJJJUzXUJn)cC{
import time
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qt_material import *
from View.HomeView import Ui_Home
from Controller.AboutController import *
from Controller.EditController import *
from Controller.ReminderItemController import *
from Controller.DayController import *
from Model.Reminder import Data
from lunar_python import *

class HomeController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)
        with open("Resources/qss/Home.qss") as file:
            self.setStyleSheet(file.read())
        self.updateTime()
        self.timer=QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start()
        self.updateList()
        self.today=QDate().currentDate()
        self.loc=QLocale()
        self.ui.todayDate.setText(self.loc.toString(self.today,"yyyy年M月d日\ndddd"))
        self.calDate=self.today
        self.updateCalendar(0)

    def mousePressEvent(self, event):
        self.isPressed = True
        self.startPos = event.globalPos()
        return QWidget().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QWidget().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.isPressed:
            movePos = event.globalPos() - self.startPos
            self.startPos = event.globalPos()
            self.move(self.pos() + movePos)
        return QWidget().mouseMoveEvent(event)

    def toAbout(self):
        self.About=AboutController()
        self.About.show()

    def updateTime(self):
        self.ui.nowTimeH.display(time.strftime("%H",time.localtime()))
        self.ui.nowTimeM.display(time.strftime("%M",time.localtime()))
        self.ui.nowTimeS.display(time.strftime("%S",time.localtime()))

    def toAddReminder(self):
        self.addReminder=EditController()
        self.addReminder.show()

    def updateList(self):
        self.ui.Reminders.clear()
        db=Data()
        datas = db.getAllReminders()
        for data in datas:
            id,title,rtime= data[0],data[1], data[2]
            w=ReminderItemController(id=id,title=title,rtime=rtime)
            item=QListWidgetItem()
            item.setSizeHint(QSize(310,64))
            w.resize(QSize(310,64))
            self.ui.Reminders.addItem(item)
            self.ui.Reminders.setItemWidget(item,w)
        db.close()
        self.getNearestAlarm()
        self.setupAlarm()

    def getDayLine2(self,date):
        solar=Solar.fromYmd(date[0],date[1],date[2])
        lunar=solar.getLunar()
        fes=solar.getFestivals()
        jieqi=lunar.getJieQi()
        lunarFes=lunar.getFestivals()
        if fes!=[] and len(fes[0])<=4:
            Line2=fes[0]
        elif jieqi!="":
            Line2=jieqi
        elif lunarFes!=[]:
            Line2=lunarFes[0]
        else:
            Line2=lunar.getDayInChinese()
            if Line2=="初一":
                Line2=lunar.getMonthInChinese()+"月"
        return Line2

    def updateCalendar(self,type=0):
        if type==0:
            self.calDate=QDate(self.today.year(),self.today.month(),1)
        elif type==-2:
            if self.calDate.year()>1970:
                self.calDate=self.calDate.addYears(-1)
        elif type==-1:
            if self.calDate.year()>1970 or (self.calDate.month()>1 and self.calDate.year()==1970):
                self.calDate=self.calDate.addMonths(-1)
        elif type==1:
            if self.calDate.year()<2199 or (self.calDate.month()<12 and self.calDate.year()==2199):
                self.calDate=self.calDate.addMonths(1)
        elif type==2:
            if self.calDate.year()<2199:
                self.calDate=self.calDate.addYears(1)
        year=self.calDate.year()
        month=self.calDate.month()
        totalDays=self.calDate.daysInMonth()
        startWeekDay=self.calDate.dayOfWeek()
        days=[""]*(startWeekDay-1)
        i=1
        while len(days)<35 and i<=totalDays:
            days.append(str(i))
            i+=1
        if i<totalDays:
            j=0
            while i<=totalDays:
                days[j]=str(i)
                j+=1
                i+=1
        while len(days)<35:
            days.append("")

        t=0
        for i in [1,2,3,4,5]:
            for j in [1,2,3,4,5,6,7]:
                if days[t]!="":
                    exec (r"self.ui.c" + str(i) + str(j) + r".date=("+str(year)+","+str(month)+","+days[t]+")")
                    Line2=self.getDayLine2((year,month,int(days[t])))
                    days[t]+="\n%s" %Line2
                eval(r"self.ui.c" + str(i) + str(j) + r".setText(days[t])")
                eval(r"self.ui.c" + str(i) + str(j) + r".isToday()")
                t+=1
        self.ui.calYear.setText(self.calDate.toString("yyyy年"))
        self.ui.calMonth.setText(self.calDate.toString("M月"))

    def backToToday(self):
        self.updateCalendar(0)
    def nextMonth(self):
        self.updateCalendar(1)
    def nextYear(self):
        self.updateCalendar(2)
    def lastMonth(self):
        self.updateCalendar(-1)
    def lastYear(self):
        self.updateCalendar(-2)

    def toDayView(self,date):
        self.dayview=DayController(date)
        self.dayview.show()

    def getNearestAlarm(self):
        db = Data()
        self.nearestReminder = db.getNearest()
        db.close()
        if self.nearestReminder != None:
            self.nearestReminderID = self.nearestReminder[0]
            self.nearestReminderTime = self.nearestReminder[3]

    def alarmOn(self):
        if int(time.time())>=self.nearestReminderTime:
            self.alarmView=DetailController(id=self.nearestReminderID,isAlarm=True)
            self.alarm.stop()
            self.getNearestAlarm()
            self.setupAlarm()
            self.alarmView.show()

    def setupAlarm(self):
        if self.nearestReminder!=None:
            self.alarm=QTimer()
            self.alarm.setInterval(900)
            self.alarm.timeout.connect(self.alarmOn)
            self.alarm.start()