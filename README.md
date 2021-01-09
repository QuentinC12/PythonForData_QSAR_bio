# Python for data analysis

dataset: http://archive.ics.uci.edu/ml/datasets/QSAR+biodegradation

Nous avons un dataset possédant 41 features et 1 target.
Notre dataset est un QSAR.
Le QSAR est une relation quantitative structure à activité,
c'est le procédé par lequel une structure chimique est corrélée avec un effet bien déterminé comme l'activité biologique ou la réactivité chimique. 
Dans notre cas ce dataset montre différentes structures chimiques corrélées avec une classe expérimentale qui reprénte la biodégradabilité de la structure chimique.

## Objectif

Notre objectif est de réaliser un modèle qui nous permettra par la suite de trouver la target (biodégradable ou non) en fonction de la structure de la molécule.
Le tout sera implementé dans une API qui permettra d'émettre des requêtes POST pour envoyer les paramètres de la structure chimique et d'obtenir une réponse sur sa classe experimentale.

![](images/image1.PNG)

### Méthode

La réalisation du modèle est passée par plusieurs étapes.
_ Visualisation des données
_ Modélisation

La visualisation des données a permis d'obtenir de nombreuses informations notamment le fait que certaines variables soient correlées entre elle.
Celle-ci ont par la suite été retirée de façon à obtenir une précision optimale.
On obtient également les résultats nous montrant les variables ayant la plus forte incidence sur le fait que la structure chimique soit biodégradable ou non.

La Modélisation s'est fait sur plusieurs classifieurs de façon à trouver celui ayant l'accuracy la plus élévée. 
Deux classifieurs ont été utilisé: 
_ Knn
_ Random Forest

### Résultats

Les résultats de notre visualisation de données nous permettent d'obtenir les features ayant la plus forte incidence sur la classe experimentale (Ready biodegradable, Not Ready biodegradable).
Résultat:

_C%

_nO

_HyWi_B(m)

_SpPosA_B(p)

_SpMax_B(m)

_SM6_B(m)

Sont les variables ayant la plus forte incidence sur notre target.

Les résultats des modélisation nous ont permis de voir que la méthode des random forest était la plus optimale pour notre dataset.
Une Gridsearch et une cross validation ont permis d'obtenir les hyperparamètres ayant la meilleure accuracy pour notre modèle.
C'est donc à l'aide de ces méthodes que nous avons obtenu un modèle se basant sur le classifieur Random Forest ayant les paramètres les plus optimaux.


## API Flask

Une API flask a été réalisée.
J'ai implémenté un endpoints se trouvant à cette adresse localhost:5000/predict
Il n'est accessible qu'en méthode POST et permet d'envoyer les features d'une structure chimique et de recevoir sa classification (RB ou NRB)
Aucun front-end n'a été implementé, de ce fait j'ai utilisé Postman pour effectuer mes requêtes.

![](images/image2.PNG)

## Utilisation de l'api avec postman

Commençons par ouvrir postman et créons une requête comme suit:
Requête à ce lien: localhost:5000/predict avec la méthode POST

![](images/image3.PNG)

Nous allons maintenant ajouter des paramètres à notre requête, ceux-ci sont la structure chimique d'une molécule que j'ai pris dans ma dataset de test.
Corps de la requête:

{
    "J_Dz(e)":-0.754206,
    "nHM":-0.480821,
    "F01[N-N]":-0.168237,
    "F04[C-N]":-0.410500,
    "NssssC":1.585458,
    "nCb-":-0.749313,
    "C%":-0.283541,
    "nCp":0.775415,
    "nO":-0.451117, 
    "F03[C-N]":-0.445567, 
    "SdssC":0.262428, 
    "HyWi_B(m)":-0.418828, 
    "LOC":-0.620738, 
    "F03[C-O]":0.081559, 
    "Me":-0.828728,
    "Mi":0.182797,
    "nN-N":-0.087464, 
    "nArNO2":-0.212861, 
    "nCRX3":-0.113205, 
    "SpPosA_B(p)":-0.169166, 
    "nCIR":0.288682, 
    "B01[C-Br]":-0.19539,
    "B03[C-Cl]":-0.421158, 
    "N-073":-0.158392, 
    "Psi_i_1d":0.032994, 
    "B04[C-Br]":-0.151849, 
    "SdO":-0.732587, 
    "TI2_L":-0.901509, 
    "nCrt":1.277714,
    "C-026":-0.588916, 
    "F02[C-N]":-0.557402, 
    "nHDon":0.028691, 
    "SpMax_B(m)":-0.221433, 
    "Psi_i_A":-0.910685, 
    "nN":-0.627501, 
    "SM6_B(m)":-0.457093,
    "nArCOOR":-0.158956, 
    "nX":-0.32553
}

![](images/image4.PNG)

Lors de l'envoi de cette requête nous obtenons le résultat suivant:

![](images/image5.PNG)

Notre molécule est donc non biodégradable.

Même principe pour une molécule biodégradable.

{
    "J_Dz(e)":-0.1552148938330818,
    "nHM":-0.48082093572289397,
    "F01[N-N]":-0.1682374430611899,
    "F04[C-N]":0.015147609361559448,
    "NssssC":-0.27991692717209804,
    "nCb-":0.1530739135469291,
    "C%":0.21057861062382474,
    "nCp":0.2908523469028476,
    "nO":-1.021269929290358, 
    "F03[C-N]":0.18149982219684982, 
    "SdssC":0.2624283649851538, 
    "HyWi_B(m)":-0.5069777794352162, 
    "LOC":-0.18862537200328958, 
    "F03[C-O]":-0.8027435509790835, 
    "Me":-0.8509477186192447,
    "Mi":-0.022941184396142053,
    "nN-N":-0.08746434675422707, 
    "nArNO2":-0.21286105660236668, 
    "nCRX3":-0.11320502839602563, 
    "SpPosA_B(p)":0.31726369165919055, 
    "nCIR":-0.08832631474678228, 
    "B01[C-Br]":-0.19539022468250006,
    "B03[C-Cl]":-0.4211582857738616, 
    "N-073":-0.15839191898578664, 
    "Psi_i_1d":0.09355003057533975, 
    "B04[C-Br]":-0.15184943999628206, 
    "SdO":-0.7325872647566545, 
    "TI2_L":-0.4438890461033984, 
    "nCrt":-0.20387178484412766,
    "C-026":0.09490802351194985, 
    "F02[C-N]":0.3453641100752494, 
    "nHDon":0.8349140876514355, 
    "SpMax_B(m)":-0.26180330606915536, 
    "Psi_i_A":-0.7582022692125185, 
    "nN":0.29891445487492024, 
    "SM6_B(m)":-0.4206738172904736,
    "nArCOOR":-0.15895646195030355, 
    "nX":-0.3255304439305592
}

![](images/image6.PNG)

![](images/image7.PNG)

notre molécule est donc biodégradable.







