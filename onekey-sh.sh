alias a="alias "
alias b="pbcopy"
alias bd=". bd -si"
alias bs="brew search --desc "
alias bi="brew install"
alias bin="brew install"
alias c="ccat"
alias cl="clear"
#alias d=	当前工作目录
alias e="echo"
alias f="find"
alias fname="find . -name '*' | grep $* "
alias xfname="mdfind -onlyin . -name"
# 搜索文件内容
alias fs='_gfile(){ grep -nE $2 $1 }; _gfile $1 $2'

# alias g=	git
# alias h= 	历史记录
alias hc="fc -l -n 1 | grep  $*"
alias i=""
# alias j=  autojump
alias k=""
alias l="ls"
alias log="adb logcat -v threadtime| grep -E --color $*"
alias logp='_logp(){ echo 111}; _logp() $1'
alias lspath='lspath.py'
alias lr="ls -a | grep"
alias m="move"
alias mux="tmuxinator"
alias n="touch"
alias o="open"
alias of="open `pwd`"
alias p="pwd"
alias py="python2.7"
alias q=""
alias r="grep "
alias s="subl"
# alias t= tail
alias u="unalias"
alias v="vim"
alias w="which"
alias x="xargs"
alias y="where"
# alias z=列举最常用的工作目录
