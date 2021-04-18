<template>
  <div class="equipes">
   
    <div class="all">
      <div class="top_l">
        <div class="equipe">
            <b-card title="Traitement Automatique des Langues et Contenus Numériques" sub-title="Responsable de l’équipe: Dr. Hassina Aliane">
              <b-card-text>
                Le développement des grands volumes d’information sur le web rend aujourd’hui crucial le besoin en ressources et outils de TAL. Dans  ce contexte l'équipe TAL  et Contenus Numériques s'intéresse à l'étude et la compréhension des mécanismes des langues naturelles dans le but d'offrir des outils de qualité pour différentes applications clés dans le domaine du traitement des grands corpus numériques. L'équipe s'intéresse particulièrement à la langue Arabe (et ses dialectes) et se fixe pour objectif d’offrir des outils aux sciences humaines et sociales pour contribuer à une meilleure appropriation des TIC par cette communauté d'une part et contribuer à limiter le fossé numérique d'autre part.

Les travaux de l'équipe portent notamment sur les thématiques suivantes:

Développement de corpus et de ressources linguistiques (dictionnaires, ontologies,..)
Outils TAL pour le web sémantique et  le big data
Développent d'applications: Résumé automatique en langue arabe, extraction de connaissances et peuplement d’ontologies en langue arabe, traduction automatique, analyse de sentiments, Système de Question Réponse, Système de Recommandation …
              </b-card-text>
            </b-card>
        </div>
      </div>
      <div class="top_r">
        <div class="equipe">
          <b-card title="Mathématique et Apprentissage Automatique pour le traitement de l’information" sub-title="Responsable de l’équipe: Merazka Mustapha">
              <b-card-text>
              </b-card-text>
            </b-card>
        </div>
      </div>

      <div class="top_l">
        <div class="equipe">
            <b-card title="Modes d’accès et de diffusion de l’information" sub-title="Responsable de l’équipe: Aliouali Nadia">
              <b-card-text>
                L'impact des technologies des communications et de l'informatique se fait de plus en plus sentir sur l'information scientifique et technique et les professionnels qui y œuvrent. Ces
vingt-cinq dernières années ont été l'occasion de changements considérables dans le secteur, et qui vont se maintenir au cours des décennies qui viennent.
L’organisation de l’information scientifique et technique (IST) est un enjeu tant du côté de la communauté des chercheurs que du côté des professionnels de l’information.
La gestion de l’IST (création, collecte, stockage, traitement et diffusion) connaît depuis, quelques années une véritable révolution sous la pression des nouvelles technologies et des nouvelles potentialités du numérique.

Dans ce contexte, le rôle de l’équipe « Mode d’accès et de diffusion de l’information »est de développer des recherches en relation avec les sciences de l’information et des bibliothèques. L’objectif de l’équipe et de superviser, coordonner et conduire des projets en liens avec les nouveaux modes de diffusion et d’accès à l’IST avec une vision globale de l’ensemble des techniques et des outils disponible aujourd’hui dans le processus de production, d’organisation et de circulation des savoirs, et qui posent de nombreux défis aux professionnels au niveaux managérial, organisationnel , juridique et budgétaire.

Les travaux de l'équipe portent notamment sur les thématiques suivantes:

Description et organisation de l’information
Normes et formats de données
Production de contenu numérique
Open Access
Préservation et archivage
Aspects juridiques liées aux documents numériques
Economie de l’information
              </b-card-text>
            </b-card>
        </div>
      </div>
      <div class="top_r">
        <div class="equipe">
          <b-card title="Linked data" sub-title="Responsable de l’équipe: Nouri Leila">
              <b-card-text>
              </b-card-text>
            </b-card>
        </div>
      </div>

      <div class="top_l">
        <div class="equipe">
          <b-card title="Représentation, préservation et conservation des données" sub-title="Responsable de l’équipe: Bessai Fatma Zohra">
              <b-card-text>
              </b-card-text>
            </b-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Equipes',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

@import url(https://fonts.googleapis.com/css?family=Open+Sans);

.all {
  display : column;
}

.top_r{
  display : flex;
  flex-direction : row;
  align-items : center;
  justify-content: flex-end;
}


.top_l{
  display : flex;
  flex-direction : row;
  align-items : center;
  justify-content: flex-start;
}


.equipe {
  width: 50%;
}







/* search */

/* end search */

</style>
