for file in *.py
do
    echo -e "#!/usr/bin/python3\n$(tail -n +2 $file)" > "$file"
done

