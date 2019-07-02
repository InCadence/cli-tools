#!/bin/bash

#######################################################################################
#  Author: James Stoup
#
#  Script for changing the color and text of the security banners
# 
#  This script changes the color of the security banner located here:
#
#  /opt/glassfish4/glassfish/domains/ion/applications/ion-browser-<version>/css/banner.css
# 
#  The text for the banner will also get changed in every HTML file that has a banner.
#  Those files can be found here:
#  
#  /opt/glassfish4/glassfish/domains/ion/applications/ion-browser-<version>
#
#  As a side note, if this suddenly stops working then the version probably changed
#  and we need to update this script.
#######################################################################################

# root check
if [ "$EUID" -ne 0 ];  then 
    echo "Please run as root"
    exit
fi


BASE_PATH=/opt/glassfish4/glassfish/domains/ion/applications

BROWSER_PATH=`find $BASE_PATH -name oetscmanage.html | rev | cut -d '/' -f 2 | rev | head -1`
if [ -z "$BROWSER_PATH" ] ; then
	echo "ION is not installed. Please check that the war files are installed properly"
	exit 1
fi

BANNER_FILE_STR=css/banner.css
BANNER_FILE=$BASE_PATH/$BROWSER_PATH/$BANNER_FILE_STR

INDEX_FILE_STR=index.html
INDEX_FILE=$BASE_PATH/$BROWSER_PATH/$INDEX_FILE_STR

HTML_FILES_LOC=$BASE_PATH/$BROWSER_PATH

NEW_COLOR=green
BANNER_TEXT=""

#####################################
# Check to see if we should quit
#####################################
check_exit() {

    if [[ $1 == 'q' ]]; then
	echo ""
	echo ""
	echo "Quitting without saving changes"
	echo ""
	exit 1;
    fi
}


#####################################
# print instructions for color
#####################################
color_usage() {
    cat <<EOF
Select a new banner color

  1 - green
  2 - red
  3 - blue
  4 - yellow
  5 - orange
  6 - gray
EOF
}


#####################################
# print instructions for banner text
#####################################
text_usage() {
    cat <<EOF

Enter the banner text
EOF
}


#####################################
# select the banner color
#####################################
select_color() {
    color_usage

    number=""
    while true; do
	read number

	if [[ $number =~ ^[123456]{1}$ ]]; then
	    break
	else
	    echo "Please enter a valid selection!"
	    color_usage
	fi
    done


    case $number in 
	1) NEW_COLOR=green;;
	2) NEW_COLOR=red;;
	3) NEW_COLOR=blue;;
	4) NEW_COLOR=yellow;;
	5) NEW_COLOR=orange;;
	6) NEW_COLOR=gray;;
    esac
}

#####################################
# enter the banner text
#####################################
enter_text() {
    text_usage
    read BANNER_TEXT
}


#####################################
# confirm changes
#####################################
confirm_changes() {
    echo ""
    echo "NEW BANNER COLOR : $NEW_COLOR"
    echo "NEW BANNER TEXT  : $BANNER_TEXT"
    echo ""

    echo "Write changes to ION?"
    REPLY=""
    while read -n1 -r -p "choose [y]es | [q]uit " && [[ $REPLY != [ynq] ]]; do
	case $REPLY in
	    *) echo "\nPlease enter y or q!";;
	esac
    done

    check_exit $REPLY
}


#####################################
# write changes to the files
#####################################
write_changes() {
    echo ""
    echo ""
    echo "writing changes"

    # change the background color
    sed -i  "s/background-color:.*/background-color: $NEW_COLOR;/" $BANNER_FILE

    # change the banner text
    SEARCH_STR="\<span class\=security_banner\>"
    BANNER_TEXT=$(echo "$BANNER_TEXT" | sed 's/\//\\\//g')

    if [ "$(grep -c "$SEARCH_STR" "$INDEX_FILE")" -ge 1 ]; then
	sed -i "s/<span class=security_banner>.*<\/span>/<span class=security_banner>$BANNER_TEXT<\/span>/" $HTML_FILES_LOC/*.html
    else
	sed -i "s/<strong>.*<\/strong>/<strong><span class=security_banner>$BANNER_TEXT<\/span><\/strong>/" $HTML_FILES_LOC/*.html
    fi
}


#####################################
# run everything
#####################################
select_color
enter_text
confirm_changes
write_changes

