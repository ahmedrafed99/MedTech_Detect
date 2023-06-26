$(document).ready(function() {
    // Sélectionner le formulaire de prédiction
    const form = $('#sepsis-form');
    
    // Écouter l'événement de soumission du formulaire
    form.on('submit', function(e) {
        e.preventDefault();

        // Récupérer les valeurs des champs de saisie
        const prg = $('#prg').val();
        const pl = $('#pl').val();
        const pr = $('#pr').val();
        const sk = $('#sk').val();
        const ts = $('#ts').val();
        const m11 = $('#m11').val();
        const bd2 = $('#bd2').val();
        const age = $('#age').val();
        const insurance = $('#insurance').val();

        // Créer un objet avec les données
        const data = {
            PRG: prg,
            PL: pl,
            PR: pr,
            SK: sk,
            TS: ts,
            M11: m11,
            BD2: bd2,
            Age: age,
            Insurance: insurance
        };

        // Prétraiter les données
        const preprocessedData = preprocessData(data);

        // Envoyer une requête AJAX à l'API de prédiction
        $.ajax({
            url: '/predict/patient',
            method: 'POST',
            data: preprocessedData,
            success: function(response) {
                // Afficher le résultat de la prédiction
                const resultContainer = $('#result-container');
                resultContainer.text('Résultat de la prédiction : ' + response.prediction);
            },
            error: function(error) {
                // Afficher une erreur en cas de problème de prédiction
                const resultContainer = $('#result-container');
                resultContainer.text('Erreur lors de la prédiction : ' + error.responseJSON.message);
            }
        });
    });
});

function preprocessData(data) {
    // Supprimer les colonnes non pertinentes
    delete data.ID;
    delete data.Insurance;
    // Remplacer les valeurs dans la colonne Sepsis
    data.Sepsis = data.Sepsis === 'Negative' ? 0 : 1;

    return data;
}
