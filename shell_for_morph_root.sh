#To run : sh shell_for_morph_root.sh <Temp folder name>
echo > $HOME_anu_tmp/tmp/$1/Hroot_missing_log
i=1
n=102 #`ls -d */ | wc -l`
#n=86
current=`pwd`
#echo "$current"
while [ $i -le $n ]
do
        sentence_dir='2.'$i
        #echo $sentence_dir
        tmp_path=$HOME_anu_tmp/tmp/$1/$sentence_dir
        python $HOME/3Task/generate_root.py  $tmp_path/hindi.morph.dat $tmp_path/hindi_dep_parser_original.dat #change the path acc. to the location of generate_root.py 
        echo $sentence_dir >> $HOME_anu_tmp/tmp/$1/Hroot_missing_log
	cat $tmp_path/morph_and_parser_root_info_log >> $HOME_anu_tmp/tmp/$1/Hroot_missing_log
	i=`expr $i + 1`
done


