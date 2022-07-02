# 冰雪聪明！
# -------------------------------------------------------
# @By:Kohaku Cao
# @Time:2022-06-26 20:39
# @QQ:1848790911
# @Mail:kohaku@hepnovel.com
# @File:DayController.py
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
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qt_material import *
from View.DayView import Ui_Day
from Model.Reminder import Reminder
from Controller.ReminderItemController import *
import time
from lunar_python import *

class DayController(QWidget):
    def __init__(self,date):
        super().__init__()
        self.date=date
        self.ui = Ui_Day()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)
        with open("Resources/qss/Day.qss") as file:
            self.setStyleSheet(file.read())
        self.otherInfoText=""  #初始化右侧的内容

        #获取农历日期，节气，阳历阴历节日和纪念日信息并显示
        solar = Solar.fromYmd(date[0], date[1], date[2])
        lunar = solar.getLunar()
        fes = solar.getFestivals()
        jieqi = lunar.getJieQi()
        lunarFes = lunar.getFestivals()
        otherDays=solar.getOtherFestivals()
        self.otherInfoText+=lunar.getYearInGanZhi()+"年"+lunar.getMonthInChinese()+"月"+lunar.getDayInChinese()
        if jieqi!="":
            self.otherInfoText+="\n%s" %jieqi
        if fes!=[]:
            i="，".join(s for s in fes)
            self.otherInfoText+="\n%s" %i
        if lunarFes!=[]:
            i="，".join(s for s in lunarFes)
            self.otherInfoText+="\n%s" %i
        if otherDays!=[]:
            i="，".join(s for s in otherDays)
            self.otherInfoText+="\n%s" %i
        self.ui.otherInfo.setText(self.otherInfoText)

        self.ui.yearLabel.setText("%d年" %date[0])
        self.ui.dayTitle.setText("%d年%d月%d日" %(date[0],date[1],date[2]))
        self.setWindowTitle("%d年%d月%d日" %(date[0],date[1],date[2]))
        self.ui.dayLabel.setText("%d月%d日" %(date[1],date[2]))
        self.updateList()

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

    def updateList(self):
        '''
        更新备忘录列表
        :return:
        '''
        self.ui.Reminders.clear()
        r=Reminder(date=self.date)
        datas = r.getRemindersByDate()
        for data in datas:
            id,title,rtime= data[0],data[1], data[2]
            w=ReminderItemController(id=id,title=title,rtime=rtime,fr="Day")
            item=QListWidgetItem()
            item.setSizeHint(QSize(430,64))
            w.resize(QSize(430,64))
            self.ui.Reminders.addItem(item)
            self.ui.Reminders.setItemWidget(item,w)
        r.close()

    def addReminder(self):
        '''
        打开新建备忘录窗口
        :return:
        '''
        self.addReminderView = EditController(fr="Day")
        self.addReminderView.show()