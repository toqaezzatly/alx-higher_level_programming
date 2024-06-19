for file in *.js
do
    echo  "#!/usr/bin/node\n$(cat $file)" > "$file"
done

