/*
 * Papier.h
 *
 *  Created on: 25 sept. 2019
 *      Author: 3670958
 */

#ifndef HEADERS_PAPIER_H_
#define HEADERS_PAPIER_H_
#include "document.h"
class Papier : public Document{
private:
	string auteur,editeur;
public:
	Papier(bool pro,int date);
	friend ostream & operator<<(ostream &os, const Papier &Papier ) ;
	const string& getAuteur() const;
	void setAuteur(const string& auteur);
	const string& getEditeur() const;
	void setEditeur(const string& editeur);
};




#endif /* HEADERS_PAPIER_H_ */
