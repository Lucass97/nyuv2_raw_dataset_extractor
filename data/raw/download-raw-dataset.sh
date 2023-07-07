#!/bin/bash

# Colors
Red='\e[0;31m';
BRed='\e[1;31m';
BIRed='\e[1;91m';
Gre='\e[0;32m';
BGre='\e[1;32m';
BBlu='\e[1;34m';
BWhi='\e[1;37m';
RCol='\e[0m';

# Function to download a file
download_file() {
    url=$1
    filename=$(basename "$url")

    # Check if file exists
    if [ -f "$filename" ]; then
        echo -e "${BBlu}Skipping $filename. File already exists.${RCol}"
    else
        # Print colored message
        echo -e "${BBlu}Downloading $filename...${RCol}"
        wget --no-verbose --show-progress "$url" -O "$filename"
    fi
}

# Function to calculate MD5
calculate_md5() {
    expected_md5_file=$1

    expected_md5=$(cat "$expected_md5_file" | awk '{print $1}')
    file=$(cat "$expected_md5_file" | awk '{print $2}')

    echo -e "${BBlu}Calculating MD5 for $file...${RCol}"
    calculated_md5=$(md5sum "$file" | awk '{print $1}')

    if [ "$calculated_md5" = "$expected_md5" ]; then
        echo -e "${BGre}MD5 verification successful for $file.${RCol}"
    else
        echo -e "${BRed}MD5 verification failed for $file.${RCol}"
    fi
}


# Basements
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/basements.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/basements.md5"

calculate_md5 "basements.md5"




# Bathrooms (1/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part1.md5"

calculate_md5 "bathrooms_part1.md5"

# Bathrooms (2/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part2.md5"

calculate_md5 "bathrooms_part2.md5"

# Bathrooms (3/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part3.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part3.md5"

calculate_md5 "bathrooms_part3.md5"

# Bathrooms (4/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part4.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part4.md5"

calculate_md5 "bathrooms_part4.md5"




# Bedrooms (1/7)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part1.md5"

calculate_md5 "bedrooms_part1.md5"

# Bedrooms (2/7)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part2.md5"

calculate_md5 "bedrooms_part2.md5"

# Bedrooms (3/7)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part3.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part3.md5"

calculate_md5 "bedrooms_part3.md5"

# Bedrooms (4/7)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part4.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part4.md5"

calculate_md5 "bedrooms_part4.md5"

# Bedrooms (5/7)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part5.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part5.md5"

calculate_md5 "bedrooms_part5.md5"

# Bedrooms (6/7)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part6.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part6.md5"

calculate_md5 "bedrooms_part6.md5"

# Bedrooms (7/7)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part7.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part7.md5"

calculate_md5 "bedrooms_part7.md5"




# Bookstore (1/3)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part1.md5"

calculate_md5 "bookstore_part1.md5"

# Bookstore (2/3)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part2.md5"

calculate_md5 "bookstore_part2.md5"

# Bookstore (3/3)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part3.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part3.md5"

calculate_md5 "bookstore_part3.md5"




# Cafe
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/cafe.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/cafe.md5"

calculate_md5 "cafe.md5"




# Living rooms (1/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part1.md5"

calculate_md5 "living_rooms_part1.md5"

# Living rooms (2/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part2.md5"

calculate_md5 "living_rooms_part2.md5"

# Living rooms (3/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part3.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part3.md5"

calculate_md5 "living_rooms_part3.md5"

# Living rooms (4/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part4.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part4.md5"

calculate_md5 "living_rooms_part4.md5"




# Dining rooms (1/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part1.md5"

calculate_md5 "dining_rooms_part1.md5"

# Dining rooms (2/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part2.md5"

calculate_md5 "dining_rooms_part2.md5"

# Dining rooms (3/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part3.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part3.md5"

calculate_md5 "dining_rooms_part3.md5"

# Dining rooms (4/4)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part4.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part4.md5"

calculate_md5 "dining_rooms_part4.md5"




# Furniture_stores
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/furniture_stores.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/furniture_stores.md5"

calculate_md5 "furniture_stores.md5"




# Home Offices
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/home_offices.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/home_offices.md5"

calculate_md5 "home_offices.md5"




# Kitchens (1/3)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part1.md5"

calculate_md5 "kitchens_part1.md5"

# Kitchens (2/3)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part2.md5"

calculate_md5 "kitchens_part2.md5"

# Kitchens (3/3)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part3.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part3.md5"

calculate_md5 "kitchens_part3.md5"




# Libraries
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/libraries.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/libraries.md5"

calculate_md5 "libraries.md5"



# Studies
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/studies.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/studies.md5"

calculate_md5 "studies.md5"




# Misc (1/2)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/misc_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/misc_part1.md5"

calculate_md5 "misc_part1.md5"

# Misc (2/2)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/misc_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/misc_part2.md5"

calculate_md5 "misc_part2.md5"




# Offices (1/2)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/offices_part1.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/offices_part1.md5"

calculate_md5 "offices_part1.md5"

# Offices (2/2)
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/offices_part2.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/offices_part2.md5"

calculate_md5 "offices_part2.md5"




# Office kitchens
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/office_kitchens.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/office_kitchens.md5"

calculate_md5 "office_kitchens.md5"




# Playrooms
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/playrooms.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/playrooms.md5"

calculate_md5 "playrooms.md5"




# Reception Rooms
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/reception_rooms.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/reception_rooms.md5"

calculate_md5 "reception_rooms.md5"




# Study Rooms
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/study_rooms.zip"
download_file "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/study_rooms.md5"

calculate_md5 "study_rooms.md5"