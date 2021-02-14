
# 本文件主要是为配置java的环境变量
JAVA_HOME="/Applications/Android Studio.app/Contents/jre/jdk/Contents/Home"

PATH=$JAVA_HOME/bin:$PATH:.

CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:.

export JAVA_HOME

export PATH

export CLASSPATH

# 配置完成后使用以下指令进行测试: java -version 