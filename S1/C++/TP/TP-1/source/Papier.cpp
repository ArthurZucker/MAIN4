#include "../Headers/Papier.h"

const string& Papier::getAuteur() const {
	return auteur;
}

void Papier::setAuteur(const string& auteur) {
	this->auteur = auteur;
}

const string& Papier::getEditeur() const {
	return editeur;
}

Papier::Papier(bool pro,int date) : Document(pro,date){

}

void Papier::setEditeur(const string& editeur) {
	this->editeur = editeur;
}

ostream & operator<<(ostream &os, const Papier &Papier ){
	os << "Editeur: "<<Papier.editeur;
	return os;
}