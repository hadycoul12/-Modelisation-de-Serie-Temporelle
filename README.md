 # 📊CRISP-DM du Projet: Préduction de prix des actions de Tesla 
 
 ## 1. Compréhension du métier
 L’objectif principal est de prédire le prix des actions de Tesla à partir de données boursières historiques. Cette prédiction peut aider les
 investisseurs à prendre de meilleures décisions d’achat ou de vente. Les parties prenantes attendent des modèles précis et exploitables,
 capables d'anticiper les tendances du marché dans un environnement financier volatil.
 
 ## 2. Compréhension des données
 Les données proviennent de Yahoo Finance, incluant les prix de clôture de Tesla (TSLA_Close) et d'autres grandes entreprises
 technologiques comme AMZN_Close, GOOGL_Close, NVDA_Close, etc. Les premières analyses exploratoires ont permis d'identifier les
 variables fortement corrélées avec Tesla, utiles comme exogènes dans les modèles (ex. : AMZN, GOOGL, NVDA).
 
 ## 3. Préparation des données
 Traitement des valeurs manquantes
 Normalisation et découpage temporel des séries
 Transformation des données pour les adapter aux modèles de séries temporelles
 Création de variables exogènes (données auxiliaires liées à d'autres actions)
 
 ## 4. Modélisation
 4 types de modèles ont été expérimentés :
 ARIMA,SARIMA :
 SARIMAX : Modèle classique de séries temporelles avec données exogènes. Il donne de bons résultats sur les tendances générales.
 
 Prophet : Modèle de Facebook performant pour détecter les tendances et saisonnalités. Il a donné les meilleurs scores de précision.
 
 LSTM (Long Short-Term Memory) : Réseau de neurones récurrent, utile pour capturer les dépendances temporelles non linéaires. Le
 modèle LSTM n’a pas été concluant dans cette version à cause d’un faible score R².
 
 ## 5. Évaluation
 Les modèles ont été comparés à l’aide de plusieurs métriques :
 MAE, RMSE, MAPE : pour évaluer l'erreur de prédiction.
 R² : pour mesurer la proportion de variance expliquée.
 
 ## 6. Déploiement / Plan d’action
 Le modèle Prophet peut être intégré à une interface de visualisation ou à une application pour :
 Suivre l'évolution prédite des actions Tesla
 Aider les utilisateurs à anticiper les fluctuations boursières
Une documentation des résultats, visualisations et métriques est prévue dans une présentation PowerPoint pour les parties prenantes
