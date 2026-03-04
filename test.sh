#!/bin/bash


# キーワード検索
read -p "キーワードを入力してください" keyword

# test.txt の中に入力したキーワードが含まれるか確認する
if grep -q "$keyword" test.txt; then 
	echo "ヒットしました"
else
	echo "検索結果はありませんでした"
fi


read -p "解析するファイル名を入力してください" file

 awk '
 {
	 if($2 == "INFO") INFO++
	 if($2 =="ERROR") ERROR++
 }
 END {
	total = INFO + ERROR
	print "INFO:", INFO
	print "ERROR:",ERROR
	print "TOTAL:", total

}


' "$file"

#!/bin/bash

read -p "解析するファイル名を入力してください: " file

awk '
{
    count[$1]++
}

END {
    for (d in count) {
        print d, count[d] 
    }
}
' "$file"






