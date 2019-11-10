__Set up:__

`pip install httpie`

__Update:__

Get updated comments by running:

    echo "[" > comments.txt; 
    http GET https://api.github.com/repos/FOSSRIT/mismatches/comments >> comments.txt; 
    echo "," >> comments.txt; 
    http GET https://api.github.com/repos/FOSSRIT/mismatches/comments?page=2 >> comments.txt; 
    echo "," >> comments.txt; 
    http GET https://api.github.com/repos/FOSSRIT/mismatches/comments?page=3 >> comments.txt; 
    echo "," >> comments.txt; 
    http GET https://api.github.com/repos/FOSSRIT/mismatches/comments?page=4 >> comments.txt; 
    echo "," >> comments.txt; 
    http GET https://api.github.com/repos/FOSSRIT/mismatches/comments?page=5 >> comments.txt;
    echo "," >> comments.txt; 
    http GET https://api.github.com/repos/FOSSRIT/mismatches/comments?page=6 >> comments.txt;
    echo "," >> comments.txt; 
    http GET https://api.github.com/repos/FOSSRIT/mismatches/comments?page=7 >> comments.txt;
    echo "]" >> comments.txt;`

(Each query gets 30 entries, so the above gets 210 comments.  May need to add more GET calls to
get full comment set.)

Process comments by running `python process_comments.py`. 

Add new processed_comments.txt script and push to github.

