"""" UTILES : FONCTIONS """
import seaborn as sns
import matplotlib.pyplot as plt


""" Diagramme en Barre : composantes principales """
def eigplot(eig):
    eig.plot.bar(x = "Composante", y = "% variance expliquée")
    plt.axhline(y = 17, linewidth = .5, color = "dimgray", linestyle = "--")
    plt.title("Variance expliquée")
    plt.show()

""" Représentation Graphique des Variables """
def plotcerclecorrelation(components, columns, eig):
    fig, axes = plt.subplots(figsize=(5,5))
    
    #Delimitation des axes
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)

    # Tracez les flèches représentant les charges des variables
    for i, (comp1, comp2) in enumerate(zip(components[0], components[1])):
        plt.arrow(0, 0, comp1, comp2, color='r', alpha=0.5, head_width=0.1)
        plt.text(comp1, comp2, columns[i], color='b', fontsize=12, ha='center', va='center')

    #on ajoute un cercle de corrélation
    axes.set_xlim(-1,1)
    axes.set_ylim(-1,1)
    cercle = plt.Circle((0,0),1,color='blue',fill=False)
    axes.add_artist(cercle)

    # Labels des axes
    plt.xlabel("Composante Principale 1 ({0:.0f}".format(eig.loc[0][2]) + "%)")
    plt.ylabel("Composante Principale 2 ({0:.0f}".format(eig.loc[1][2]) + "%)")
    plt.title("Cercle de corrélation 1 ({0:.0f}".format(eig.loc[0][2] + eig.loc[1][2]) + "%)")

    # Affichez le cercle de corrélation
    plt.grid()
    plt.show()
    
""" Représentation Graphique des Observations (Recettes) SANS les ID """
def plot_observations_sansid(WGI_pca_df, percent_X, percent_Y):
    plt.figure(figsize=(8, 8))
    WGI_pca_df.plot.scatter("Comp1", "Comp2")             #nuage de points
    
    plt.xlabel("Composante principale 1 ({0:.0f}".format(percent_X) + "%)")              
    plt.ylabel("Composante principale 2 ({0:.0f}".format(percent_Y) + "%)")               
    plt.suptitle("Représentation Graphique des observations ({0:.0f}".format(percent_X + percent_Y) + "%)")        
    plt.show()
    
    
""" Représentation Graphique des Observations (Recettes) AVEC les ID """
def plot_observations_avecid(WGI_pca_df, percent_X, percent_Y):
    plt.figure(figsize=(8, 8))
    fig, ax = plt.subplots()
    WGI_pca_df.plot.scatter("Comp1", "Comp2", ax = ax) # l'option ax permet de placer les points et le texte sur le même graphique

    # boucle sur les id et n'afficher que certains "id" car on en a "177 224" 
    for k in WGI_pca_df.iterrows():
        # annotation uniquement si valeur absolue sur une de 2 dimensions importantes (valeurs choisies empiriquement)
        if (abs(k[1]['Comp1']) > 6.5) | (abs(k[1]['Comp2']) > 4.5):
            ax.annotate(int(k[1]["id"]), (k[1]['Comp1'], k[1]['Comp2']), fontsize = 9)
    plt.xlabel("Composante principale 1 ({0:.0f}".format(percent_X) + "%)")              
    plt.ylabel("Composante principale 2 ({0:.0f}".format(percent_Y) + "%)")               
    plt.suptitle("Représentation Graphique des observations ({0:.0f}".format(percent_X + percent_Y) + "%)") 
    plt.show()
    
""" diagramme en barre des variables catégorielles """
def diagramme_en_barre(data, title, color):
    ax = data.plot(kind='bar', color=color )
    plt.title(title)
    for i, proportion in enumerate(data):
        ax.text(i, proportion, f'{proportion:.2%}', ha='center', va='bottom')