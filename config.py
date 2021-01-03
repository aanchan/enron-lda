#Set the number of LDA topics here
NUM_LDA_TOPICS=10
#Set the directory to where all models will be stored
#This is the same directory from which models are picked up
#for inteference
EXP_DIR='exp/v6/topics_' + str(NUM_LDA_TOPICS)

#Data processing configs
#This is the list of raw files that is input to data_process.py
DATA_FILE_LIST_PATH='lists/file_list'
#The output folder where data_process.py outputs cleaned and processed files
PROCESSED_OUTPUT_FOLDER='data/processed_files'
#Once the files have been processed, create a list of files for training
#using a Unix utility like find. This config variable is consumed in
#train_lda.py
PROCESSED_FILE_LIST_PATH='lists/processed_files_list'


