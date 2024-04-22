for file in *.py
do
    echo  "#!/usr/bin/python3\n$(cat $file)" > "$file"
done

