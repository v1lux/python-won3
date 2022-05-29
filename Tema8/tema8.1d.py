import catalog

mediile = catalog.afla_media('note.txt')
note_teze = catalog.afla_media('teze.txt')                  # refolosesc 'afla media' pt a citi si fisierul cu notele din teze
situatia_finala = catalog.afla_media_finala(mediile, note_teze)
catalog.scrie_situatia_noua(situatia_finala, 'mediile_finale.txt')
