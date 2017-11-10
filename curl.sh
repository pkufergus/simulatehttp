
file=./data/url.txt

for  x in `seq 1 2000`; do
    echo "x=$x"
    i=0
    while read line; do
        i=$(($i+1))
        if [ "$line" == "" ]; then
            continue
        fi
        echo "i=$i line=$line"
        curl -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36" $line >/dev/null 2>&1
        echo "i=$i line=$line end"
        sleep 1
    done < $file
done
