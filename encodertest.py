# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )


content = '<a href="http://baike.baidu.com/view/286305.htm" rel="nofollow" target="_blank">1965&#24180;</a>';

print content.decode()