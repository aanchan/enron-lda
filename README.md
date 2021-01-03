**Global Relay Project**
--

### Requirements
- Use the Enron email data set : https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz
- The input of the assignment is the emails in the Sent folder from the Enron dataset.
- A service than can injest email
- The service should return 
    - The sentiment of the email body
    - If the Email body is related to Enron's oil & gas business, then the output also lists each
Person or Organization mentioned. 

### Project Description      
Based on these requirements a service is written in Python. A 
single API endpoint called `/process-email` is made avaliable 
as a REST API GET endpoint. To expose the API functionality
I used the Flask Python framework using MethodViews. The MethodView
has been implemented in [views.py](views.py). The main
entry point to expose this endpoint is in [application.py](application.py). If the e-mail body 
belongs to Enron's Oil and Gas business then the JSON looks like:
```
{
  'sentiment': 'positive', 
  'topic': 'Enron Oil and Gas', 
  'entities': [('Chris Mahoney', 'PERSON'), 
               ('Continental', 'ORG'),
               ('kerr mcgee', 'PERSON'), 
               ('hess', 'PERSON'),  
               ('chris harris', 'PERSON')]
 }
```
For all other topics the response looks like this JSON.
```
{
  sentiment: negative
}
```

### To run on a local machine 
Run the following commands on a local machine using

Environment tested on Python 3.6.9, Ubuntu 18.04, pip 20.3
```
python3 -m venv env/global_relay
source env/global_relay/bin/activate
pip install --upgrade pip
pip install cython
pip install numpy
pip install --no-cache-dir -r requirements.txt
python3 -m spacy download en
```

Additionally you might have to go in to the Python REPL and install NLTK stopwords like so:
```
import nltk
nltk.download('stopwords')
```


```
export FLASK_APP=application.py
flask run
```
To send a request from a client like POSTMAN can be done
by getting this example request available as a POSTMAN collection: [here](https://www.getpostman.com/collections/54c136d8c6f9328e900f).
 
This sets up the body to have the following e-mail string :
```
"Message-ID: <18599553.1075842495069.JavaMail.evans@thyme>\nDate: Thu, 10 Feb 2000 03:29:00 -0800 (PST)\nFrom: drew.fossum@enron.com\nTo: bill.cordes@enron.com, dave.neubauer@enron.com, steven.harris@enron.com\nSubject: LRC Joint Venture\nMime-Version: 1.0\nContent-Type: text/plain; charset=us-ascii\nContent-Transfer-Encoding: 7bit\nX-From: Drew Fossum\nX-To: Bill Cordes, Dave Neubauer, Steven Harris\nX-cc: \nX-bcc: \nX-Folder: \\Drew_Fossum_Dec2000_June2001_1\\Notes Folders\\Sent\nX-Origin: FOSSUM-D\nX-FileName: dfossum.nsf\n\nI don't see any problem with this transaction since it appears to be limited \nto Louisiana assets, but the issue of whether we are impacted by the \nnoncompete agreement strikes me as a commercial call.  Please let me know if \nyou have any problem with the transaction and I will pursue it.  Thanks.  DF \n---------------------- Forwarded by Drew Fossum/ET&S/Enron on 02/10/2000 \n11:25 AM ---------------------------\n\n\n\nMichael Moran\n02/09/2000 01:58 PM\nTo: Louis Soldano/ET&S/Enron@ENRON, Dorothy McCoppin/FGT/Enron@ENRON, Phil \nLowry/OTS/Enron@ENRON\ncc:  \n\nSubject: LRC Joint Venture\n\nPlease see the attached and let me know if you have any problems so that GPG \ncan respond to Brian Redmond.\n---------------------- Forwarded by Michael Moran/GPGFIN/Enron on 02/09/2000 \n01:55 PM ---------------------------\n\n\nBrian Redmond@ECT\n02/09/2000 01:44 PM\nTo: Sherri Reinartz@ENRON, J Mark Metts/NA/Enron@Enron, Stephanie J \nHarris@ENRON_DEVELOPMENT, Rob Walls/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Rex \nRogers/Corp/Enron@Enron, Charles Cheek/Corp/Enron@ENRON, Peggy Fowler@ENRON, \nAl Alexanderson/Enron@Gateway, Rebecca P Mark/HOU/AZURIX@AZURIX, John \nAle/HOU/AZURIX@AZURIX, Mark Frevert/LON/ECT@ECT, Michael R Brown/LON/ECT@ECT, \nMichael Burke/Houston/Eott@Eott, Steve Duffy/Houston/Eott@Eott, Cliff \nBaxter/HOU/ECT@ECT, Greg Whalley/HOU/ECT@ECT, Mark E Haedicke/HOU/ECT@ECT, \nTimothy J Detmering/HOU/ECT@ECT, Bill Donovan/EPSC/HOU/ECT@ECT, Elizabeth \nLabanowski/EPSC/HOU/ECT@ECT, Stanley Horton/Corp/Enron@Enron, Michael \nMoran/ET&S/Enron@ENRON, Bill Cordes/ET&S/Enron@ENRON, Larry \nDeRoin/NPNG/Enron@ENRON, Janet Place/NPNG/Enron@ENRON, Ken Rice/Enron \nCommunications@Enron Communications, Kristina Mordaunt/Enron \nCommunications@Enron Communications, Andrew S Fastow/HOU/ECT@ECT, Scott \nSefton/HOU/ECT@ECT, Shirley A Hudler/HOU/ECT@ECT, Karen S Owens@ees, Vicki \nSharp/HOU/EES@EES, Ken Karas/EWC/Enron@Enron, Adam Umanoff/EWC/Enron@Enron, \nJoe Kishkill/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Randy \nYoung/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, James A \nHughes/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Bruce \nLundstrom/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Larry L \nIzzo/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, John \nSchwartzenburg/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Rob \nWalls/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Sanjay \nBhatnagar/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Wade \nCline/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, David \nHaug/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Frank \nStabler/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Frank \nSayre/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Rick \nBergsieker/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Lance \nSchuler-Legal/HOU/ECT@ECT, Harold Bertram/HOU/ECT@ECT\ncc:  \n\nSubject: LRC Joint Venture\n\nPlease find the attached memo summarizing a proposed joint venture between \nEnron North America and Texaco involving our respective intrastate pipeline \nassets in Louisiana (i.e., Enron's LRC pipeline).  The joint venture would \nrestrict Enron and its affiliates from pursuing certain limited business \nopportunities involving specified pipeline assets that may be competitive \nwith the joint venture.  Specifically, these assets include: \n\n(i) the Acadian Gas Pipeline System (currently ultimately owned by Shell \nPetroleum Inc. USA), \n(ii) the Cypress Gas Pipeline System (currently ultimately owned by Shell \nPetroleum Inc. USA), \n(iii) the Louisiana Intrastate Gas System (currently ultimately owned by \nAmerican Electric Power Co. Inc.), \n(iv) the Louisiana Gas System (currently ultimately owned by Conoco Inc.); \nand \n(v) the Louisiana gas pipeline assets of Koch Gateway Pipeline Co. (currently \nultimately owned by Koch Industries).  \n\nIn keeping with Enron's internal policies, we are seeking your confirmation \nthat you have no objection to the non-compete provisions in this \ntransaction.  Please feel free to call Lance Schuler, Hal Bertram or me if \nyou have any questions.\n\nRegards,\nBrian\n\n\n\n\n\n\n"
```
 to the endpoint `127.0.0.1:5000/process-email` as a GET request returning the following
response:
```
{
    "entities": [
        [
            "Michael Moran",
            "PERSON"
        ],
        [
            "GPG",
            "ORG"
        ],
        [
            "Brian Redmond",
            "PERSON"
        ],
        [
            "Enron",
            "ORG"
        ],
        [
            "Texaco",
            "ORG"
        ],
        [
            "Enron",
            "ORG"
        ],
        [
            "LRC",
            "ORG"
        ],
        [
            "Enron",
            "ORG"
        ],
        [
            "the Acadian Gas Pipeline System",
            "ORG"
        ],
        [
            "Shell  ",
            "ORG"
        ],
        [
            "Petroleum Inc. USA",
            "ORG"
        ],
        [
            "Shell  ",
            "ORG"
        ],
        [
            "Petroleum Inc. USA",
            "ORG"
        ],
        [
            "the Louisiana Intrastate Gas System",
            "ORG"
        ],
        [
            "American Electric Power Co. Inc.",
            "ORG"
        ],
        [
            "the Louisiana Gas System",
            "ORG"
        ],
        [
            "Conoco Inc.",
            "ORG"
        ],
        [
            "Koch Gateway Pipeline Co.",
            "ORG"
        ],
        [
            "Koch Industries",
            "ORG"
        ],
        [
            "Enron",
            "ORG"
        ],
        [
            "Lance Schuler",
            "PERSON"
        ],
        [
            "Hal Bertram",
            "PERSON"
        ],
        [
            "Brian",
            "PERSON"
        ]
    ],
    "sentiment": "positive",
    "topic": "Enron Oil&Gas"
}
```

On POSTMAN the following pre-request script is used:
```
let query = "Message-ID: <18599553.1075842495069.JavaMail.evans@thyme>\nDate: Thu, 10 Feb 2000 03:29:00 -0800 (PST)\nFrom: drew.fossum@enron.com\nTo: bill.cordes@enron.com, dave.neubauer@enron.com, steven.harris@enron.com\nSubject: LRC Joint Venture\nMime-Version: 1.0\nContent-Type: text/plain; charset=us-ascii\nContent-Transfer-Encoding: 7bit\nX-From: Drew Fossum\nX-To: Bill Cordes, Dave Neubauer, Steven Harris\nX-cc: \nX-bcc: \nX-Folder: \\Drew_Fossum_Dec2000_June2001_1\\Notes Folders\\Sent\nX-Origin: FOSSUM-D\nX-FileName: dfossum.nsf\n\nI don't see any problem with this transaction since it appears to be limited \nto Louisiana assets, but the issue of whether we are impacted by the \nnoncompete agreement strikes me as a commercial call.  Please let me know if \nyou have any problem with the transaction and I will pursue it.  Thanks.  DF \n---------------------- Forwarded by Drew Fossum/ET&S/Enron on 02/10/2000 \n11:25 AM ---------------------------\n\n\n\nMichael Moran\n02/09/2000 01:58 PM\nTo: Louis Soldano/ET&S/Enron@ENRON, Dorothy McCoppin/FGT/Enron@ENRON, Phil \nLowry/OTS/Enron@ENRON\ncc:  \n\nSubject: LRC Joint Venture\n\nPlease see the attached and let me know if you have any problems so that GPG \ncan respond to Brian Redmond.\n---------------------- Forwarded by Michael Moran/GPGFIN/Enron on 02/09/2000 \n01:55 PM ---------------------------\n\n\nBrian Redmond@ECT\n02/09/2000 01:44 PM\nTo: Sherri Reinartz@ENRON, J Mark Metts/NA/Enron@Enron, Stephanie J \nHarris@ENRON_DEVELOPMENT, Rob Walls/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Rex \nRogers/Corp/Enron@Enron, Charles Cheek/Corp/Enron@ENRON, Peggy Fowler@ENRON, \nAl Alexanderson/Enron@Gateway, Rebecca P Mark/HOU/AZURIX@AZURIX, John \nAle/HOU/AZURIX@AZURIX, Mark Frevert/LON/ECT@ECT, Michael R Brown/LON/ECT@ECT, \nMichael Burke/Houston/Eott@Eott, Steve Duffy/Houston/Eott@Eott, Cliff \nBaxter/HOU/ECT@ECT, Greg Whalley/HOU/ECT@ECT, Mark E Haedicke/HOU/ECT@ECT, \nTimothy J Detmering/HOU/ECT@ECT, Bill Donovan/EPSC/HOU/ECT@ECT, Elizabeth \nLabanowski/EPSC/HOU/ECT@ECT, Stanley Horton/Corp/Enron@Enron, Michael \nMoran/ET&S/Enron@ENRON, Bill Cordes/ET&S/Enron@ENRON, Larry \nDeRoin/NPNG/Enron@ENRON, Janet Place/NPNG/Enron@ENRON, Ken Rice/Enron \nCommunications@Enron Communications, Kristina Mordaunt/Enron \nCommunications@Enron Communications, Andrew S Fastow/HOU/ECT@ECT, Scott \nSefton/HOU/ECT@ECT, Shirley A Hudler/HOU/ECT@ECT, Karen S Owens@ees, Vicki \nSharp/HOU/EES@EES, Ken Karas/EWC/Enron@Enron, Adam Umanoff/EWC/Enron@Enron, \nJoe Kishkill/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Randy \nYoung/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, James A \nHughes/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Bruce \nLundstrom/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Larry L \nIzzo/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, John \nSchwartzenburg/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Rob \nWalls/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Sanjay \nBhatnagar/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Wade \nCline/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, David \nHaug/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Frank \nStabler/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Frank \nSayre/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Rick \nBergsieker/ENRON_DEVELOPMENT@ENRON_DEVELOPMENT, Lance \nSchuler-Legal/HOU/ECT@ECT, Harold Bertram/HOU/ECT@ECT\ncc:  \n\nSubject: LRC Joint Venture\n\nPlease find the attached memo summarizing a proposed joint venture between \nEnron North America and Texaco involving our respective intrastate pipeline \nassets in Louisiana (i.e., Enron's LRC pipeline).  The joint venture would \nrestrict Enron and its affiliates from pursuing certain limited business \nopportunities involving specified pipeline assets that may be competitive \nwith the joint venture.  Specifically, these assets include: \n\n(i) the Acadian Gas Pipeline System (currently ultimately owned by Shell \nPetroleum Inc. USA), \n(ii) the Cypress Gas Pipeline System (currently ultimately owned by Shell \nPetroleum Inc. USA), \n(iii) the Louisiana Intrastate Gas System (currently ultimately owned by \nAmerican Electric Power Co. Inc.), \n(iv) the Louisiana Gas System (currently ultimately owned by Conoco Inc.); \nand \n(v) the Louisiana gas pipeline assets of Koch Gateway Pipeline Co. (currently \nultimately owned by Koch Industries).  \n\nIn keeping with Enron's internal policies, we are seeking your confirmation \nthat you have no objection to the non-compete provisions in this \ntransaction.  Please feel free to call Lance Schuler, Hal Bertram or me if \nyou have any questions.\n\nRegards,\nBrian\n\n\n\n\n\n\n"
pm.environment.set('query', JSON.stringify(query));
```

With the Body being set to ``{{query}}`` and data type as `raw`
and `application/json` selected.

###### Running tests
If you have the [make](https://www.gnu.org/software/make/) utility
installed then you can run tests like so, once the virtualenv has been
loaded:
```
make test
```
##### Steps to complete a training run
- Set config variables in [config.py](config.py)
```
#Set the number of LDA topics here
NUM_LDA_TOPICS=3
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
```
- Create a list file for the raw data using find e.g. `find data/maildir -type f  > lists/file_list`
- Run [data_process.py](data_process.py) to prepare cleaned training data
- Create a list file for the processed data using find e.g. `find data/processed_files -type f  > lists/processed_file_list`
- Run [train_lda.py](train_lda.py) to create LDA models stored in `EXP_DIR`
- Run `make test` or deploy the Flask app locally to hit the `/process-email` endpoint as mentioned 
### Note on the data-set

**1. Cleaning the data set**

The data-set consists of emails in the Sent folder of multiple
Enron employees. One of the challenges in compiling and cleaning
this data is obtaining text from email-threads with conversations
between multiple people. A module called [email_processor.py](modules/email_processor.py) deals
with most of the text cleaning up with regular expressions. Regular
expressions operate at two levels in this module. One is at the 
string level to remove email headers, and the other operates on a 
per-line basis to mark lines that are suitable for text-processing.
The main function `process_email` is used in data cleaning scripts
and for data that is incoming to the `/process-email` API endpoint.
The script that does the data cleaning is [data_process.py](scripts/data_process.py). This 
script takes a list of files and outputs processed files. The file
list is typically created using a Unix utility like `find`. 

Prior to this a couple of steps were carried out:
- Only `sent` folders from the different employee email folders were
selected. Some have `sent` versus others have `sent_items` and some have 
  both. These were copied to a separate directory using the following
  `bash` command:
  ```
     mkdir -p sent 
     for file in $(find maildir -name "sent")
       do echo "copying $file"
        mkdir -p sent/$file
        cp -r $file sent/$file
     done
  ```
  
A list file was then created, called `file_list` which has been
placed in the `lists` folder. It was found that the resulting
data set has 58168 email files.

`file_list` is then used as input to a standalone script [data_process.py](data_process.py) which is
responsible for text clean-up. [data_process.py](data_process.py) uses the same 
routines from `email_processor.py` that is used for cleaning text
ingested by the REST API end-point `/process-email`.

For model training all of the cleaned up data is stored in the folder
`processed_email`. An associated list file, containing file paths called
`processed_files_list` was created using the Unix `find` utility.

Various resources were used to work with regular expressions:
- https://stackoverflow.com/questions/17874360/python-how-to-parse-the-body-from-a-raw-email-given-that-raw-email-does-not
- https://stackoverflow.com/questions/47739050/how-to-erase-forwarded-message-title-and-unwanted-content-from-body-of-enron-e
- https://github.com/ZhaiResearchGroup/enron-parser
- https://medium.com/@marin892/my-python-journey-pt-2-enron-emails-orms-and-more-f6d7b3790b26
- https://stackoverflow.com/questions/52789311/extracting-parts-of-emails-in-text-files
- https://stackoverflow.com/questions/5006716/getting-the-text-that-follows-after-the-regex-match?noredirect=1&lq=1
- https://stackoverflow.com/questions/7124778/how-to-match-anything-up-until-this-sequence-of-characters-in-a-regular-expres
- www.regex101.com


**2. Labels in the data set**

One of the aspects that makes this implementation/project a bit
challenging is that for Sentiment Analysis, Named Entity Recognition
and understanding the document content (i.e. if it belongs to Enron's
Oil and Gas business) there are no labels out of the box to enable 
supervised learning. So I tended to rely on either unsupervised
techniques or out-of-the-box and/or rule based packages to implement
some parts of this project.

There are some resources that do make labelled data available for this
data set, namely :
- [SIMS group from UC Berkeley](https://bailando.berkeley.edu/enron_email.html) which has annotated data into 12 categories
which would be useful possibly for Sentiment Analysis.
- [This Github Repo](https://github.com/jxu87/EnronEmails) where sentiments
were marked as `business` or `personal`. These seem to be manually labelled.

### Sentiment Analysis
For Sentiment Analysis since it was assumed that there were no labels,
no supervised classifiers can be trained for this problem. Upon doing a
literature survey (which was not completely thorough) I found there previous 
attempts at unsupervised sentiment analysis include rule-based algorithms,
as well as those based on proximity to words like `excellent` and `terrible`.

- [VADER](https://github.com/cjhutto/vaderSentiment) is a popular rule-based sentiment
analysis tool that works on a pre-defined dictionary or lexicon. It is demonstrated 
  to work well on social media and email text. This is the package I used straight out
  of the box for Sentiment Analysis. VADER seems to work well at the sentence level
  though it needs more thought to work on a paragraph level. A crude approximation
  I used as a quick-and-dirty implementation for this project was to aggregate the 
  "compound" sentence level sentiments over an e-mail and apply to it the same 
  thresholds that work on a sentence level namely:
  ```
  positive sentiment: compound score >= 0.05
  neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
  negative sentiment: compound score <= -0.05
  ```
  This clearly could be improved. The main code for Sentiment Analysis appears in
  the module [sentiment.py](modules/sentiment.py).
- An interesting research paper which has been heavily cited by
Peter Turney named [Thumbs Up or Thumbs Down? Semantic Orientation
  Applied to Supervised Classification of Reviews](https://www.aclweb.org/anthology/P02-1053.pdf)
  has the potential to be worked upon in the context of more recent work 
  on developing word embeddings like word2vec, GloVE, BERT to name a few.
    - This brought up the interesting question of whether these spaces 
      are well-behaved where notions of distance are symmetric (the term
      for this might be a metric space) and one could work with developing
      a principled method of similarity akin to the Pointwise Mutual Information
      distance measure that this paper uses in Eq. 1.
    - To this end, I found that the [Word Mover's Distance](https://github.com/mkusner/wmd)
      (WMD) published I believe in NeurIPS 2015 is a promising direction. Furthermore,
      WMD could also be used for unsupervised (or lightly supervised with a few exemplars) 
      clustering of documents.
      
Quite a few resources were visited. Of note that have not been mentioned are:
- http://www.nltk.org/howto/sentiment.html
- https://towardsdatascience.com/how-i-used-machine-learning-to-classify-emails-and-turn-them-into-insights-efed37c1e66
- [Sentiment Analysis using Unlabled Email data](https://easychair.org/publications/preprint_download/HkRB)

### Entity Extraction
For Entity extraction again, nothing novel was done as a part of this project. Spacy
was used out of the box to determine named entities in an e-mail. Spacy is also used for
topic extraction. The implementation in this project is perhaps not the most efficient
with importing and calling Spacy twice over in the code. The main code for entity extraction
appears in [entities.py](modules/entities.py).

### Topic Extraction - Unsupervised Document Clustering
Topic extraction was chosen with Latent Dirichlet Allocation (LDA) after considering 
approaches like k-Means clustering or techniques in a similar vein. One of the advantages
or by-products of LDA is document clustering into various topics. To create LDA topic
models the Gensim library was used and [this blog post](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)
was followed. This solution exercise does borrow code from this blog post and is referenced
in the comments. 

####Training LDA models
Models were created using the script [train_lda.py](train_lda.py). The folder that contains
the final model is in [exp/v6/topics_5](exp/v6/topics_5). This is also set as a config
folder name is also set as a config variable in [config.py](config.py). The number of topics
is also set in this [config.py](config.py) file. The config file is also used to specify the
path to the list of processed files.

####Text feature processing for LDA models
Additional text feature processing is carried out prior to LDA training and inference. This is all in the module [lda_data_processing.py](modules/lda/lda_data_processing.py)
Each e-mail  document is collapsed to a single line string without new-line characters. The steps to pre-processing are as follows:
- Use gensim's simple_preprocess to remove punctuations, convert to lowercase, remove apostrophes
and text normalize the word tokens in a document
- Lemmatize using Spacy's  lemmatizer
- Removing stop words

Initially when training models, data cleaning with regular expressions took a fair amount
of time and given importance. While creating the LDA models I was also using bigram and trigram
features. In the end, I did not use these features in order to save computational time since 
gensim.Phraser seems to be very expensive computationally when calculating bi-grams and tri-grams.
Therefore, these routines do not appear in the code.

A couple of things that seemed important to do was that topics seemed to be created
with high frequency tokens that yield very little value. These were words that were added to the
stop word list like - `'thank','know','go','may','let', 'need', 'call','time','make','get','deal',
'say','work','see','send','think','agreement','also','attach','want'`. These are all words that had
a count of above 12,000 occurences. `thank` alone was at 23753. Furthermore, I was applying the
stop words prior to lemmatization. This turned out to not have the intended effect since words
like `thanks` that were not lemmatized any was not a stop-word (only `thank`  is listed as a stop word).
The jury is out on whether it is better to do this pre or post lemmatization, I did it after since it 
removes any stop words from appearing post-lemmatization. The frequency of these 
tokens after lemmatization and stop-word removal are available in the pickle file [exp/v6/topics_5/freq_corpus.pkl](exp/v6/topics_5/freq_corpus.pkl).

Topic models were trained for 2,4, 5, 10 and 20 topics. Of all of these the highest
coherence score was obtained for a model with 5 topics with a coherence score of 0.523 
(Reference log-file : [model.log](exp/v6/topics_5/model.log)). The higher the coherence
score the lesser the topic overlap. The visualization for this models is available [here](https://htmlpreview.github.io/?https://github.com/aanchan/enron-lda/blob/main/exp/v6/topics_5/LDA_Visualization.html)

There is a disadvantage here though, since there can  be documents with extremely rare terms. Here is an example of a [NSFW email](/home/aanchan/work/global_relay/src/data/maildir/lenhart-m/sent/sent/780.) 
whose expletive filled terms occur only a few hundred times in the corpus. To allow for more
specificity for the purpose of this exercise a model with 10 topics. This does mean that there
is greater overlap in the topics of this model and hence a lower coherence score of 0.43. (Reference log-file : [model.log](exp/v6/topics_10/model.log)).
This visualization for this topic model is available [here](https://htmlpreview.github.io/?https://github.com/aanchan/enron-lda/blob/main/exp/v6/topics_10/LDA_Visualization.html).
The topics appear as follows.

```
(0, '0.039*"trade" + 0.038*"product" + 0.038*"counterparty" + 0.035*"trading" + 0.031*"company" + 0.027*"financial" + 0.015*"future" + 0.014*"energy" + 0.012*"customer" + 0.012*"new"')
(1, '0.062*"price" + 0.061*"gas" + 0.045*"power" + 0.041*"month" + 0.024*"period" + 0.022*"swap" + 0.019*"day" + 0.019*"volume" + 0.016*"term" + 0.016*"rate"')
(2, '0.050*"master" + 0.048*"information" + 0.043*"name" + 0.040*"email" + 0.033*"mail" + 0.032*"receive" + 0.028*"click" + 0.026*"copy" + 0.025*"access" + 0.024*"message"')
(3, '0.056*"credit" + 0.042*"shall" + 0.037*"form" + 0.034*"transaction" + 0.033*"request" + 0.032*"contract" + 0.031*"date" + 0.031*"approve" + 0.028*"execute" + 0.020*"letter"')
(4, '0.020*"member" + 0.017*"group" + 0.016*"report" + 0.015*"business" + 0.015*"team" + 0.014*"year" + 0.012*"new" + 0.011*"provide" + 0.010*"employee" + 0.010*"process"')
(5, '0.050*"book" + 0.042*"password" + 0.033*"tax" + 0.027*"presentation" + 0.021*"side" + 0.019*"ect" + 0.019*"sound" + 0.019*"bill" + 0.018*"recommendation" + 0.017*"invoice"')
(6, '0.060*"approval" + 0.032*"database" + 0.027*"order" + 0.023*"referenced" + 0.021*"state" + 0.018*"issue" + 0.017*"purchase" + 0.016*"index" + 0.013*"law" + 0.013*"settlement"')
(7, '0.043*"assignment" + 0.043*"bad" + 0.037*"ticket" + 0.033*"asap" + 0.027*"special" + 0.026*"vice" + 0.025*"season" + 0.024*"game" + 0.021*"ca" + 0.018*"nice"')
(8, '0.023*"good" + 0.019*"take" + 0.018*"come" + 0.016*"back" + 0.015*"day" + 0.014*"week" + 0.013*"well" + 0.013*"way" + 0.012*"hope" + 0.011*"tell"')
(9, '0.027*"list" + 0.022*"question" + 0.022*"regard" + 0.017*"change" + 0.016*"forward" + 0.014*"sign" + 0.013*"like" + 0.013*"legal" + 0.013*"copy" + 0.013*"file"')
```

For this particular model any email belonging to topics with index 0 or 1 are taken to belong
to `Enron Oil and Gas`. 

A take-away from this exercise is that LDA on its own is perhaps limited. A level on top of this
using LDA as sparse feature vectors with some supervised labels to generate a logistic regression
classifier could be more useful. Furthermore, [LabeledLDA](https://nlp.stanford.edu/pubs/llda-emnlp09.pdf) or 
[DependencyLDA](https://arxiv.org/abs/1107.2462) might be alternatives to try where with _some_ supervised data the LDA process can be "guided".
Supervised variants like MedLDA could also be tried. There is a slew of recent work on topic
models using deep learning which could also be competitive.




