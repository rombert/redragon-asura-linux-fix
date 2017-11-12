#!/bin/sh

hidrd_convert=../../oss/hidrd/src/hidrd-convert

txt_files=$(ls -1 hid-descriptors | grep txt)
for txt_file in $txt_files; do
    base=${txt_file%.txt}
    if [ ! -e hid-descriptors/${base}.spec ]; then
        cat hid-descriptors/$txt_file | xxd -r -p | ${hidrd_convert} -o spec > hid-descriptors/${base}.spec
    fi
    if [ ! -e hid-descriptors/${base}.bin ]; then
        cat hid-descriptors/$txt_file | xxd -r -p | ${hidrd_convert} -o natv > hid-descriptors/${base}.io
    fi

done
