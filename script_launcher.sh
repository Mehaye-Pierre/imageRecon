python3.5 make_ann.py
cd ./libsvm-3.22/
python3.5 make_model.py
python3.5 make_predict.py
cd ..
python3.5 make_top.py
cd ./trec_eval.9.0/
python3.5 make_trec_eval.py
