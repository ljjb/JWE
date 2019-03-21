mkdir -p "$1"
./jwe -train zhwiki_corpus.txt -output-word "$1/word_vec" -output-char "$1/char_vec" -output-comp "$1/comp_vec" -size 200 -window 5 -sample 1e-4 -negative 10 -iter 100 -threads 8 -min-count 1 -alpha 0.025 -binary 0 -comp "../${1}-subcharacter/comp.txt" -char2comp "../${1}-subcharacter/char2comp.txt" -join-type 1 -pos-type 1 -average-sum 1
