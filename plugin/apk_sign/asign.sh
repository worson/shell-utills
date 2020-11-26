echo "start sign ...."
# echo $@
sh_current_path=`dirname $0`
java -jar $sh_current_path/signapk.jar $sh_current_path/platform.x509.pem $sh_current_path/platform.pk8 $@