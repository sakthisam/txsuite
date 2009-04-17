/*
 * compiler/back-ends/c-gen/rules.c - initialized c rule structure
 *           inits a table that contains info about
 *           converting each ASN.1 type to C type
 * Copyright (C) 1991, 1992 Michael Sample
 *            and the University of British Columbia
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * $Header: /usr/app/odstb/CVS/snacc/compiler/back-ends/c-gen/rules.c,v 1.3 1995/07/25 18:46:34 rj Exp $
 * $Log: rules.c,v $
 * Revision 1.3  1995/07/25 18:46:34  rj
 * file name has been shortened for redundant part: c-gen/c-rules -> c-gen/rules.
 *
 * Revision 1.2  1994/09/01  00:24:35  rj
 * snacc_config.h removed.
 *
 * Revision 1.1  1994/08/28  09:48:35  rj
 * first check-in. for a list of changes to the snacc-1.1 distribution please refer to the ChangeLog.
 *
 */

#include "asn-incl.h"
#include "asn1module.h"
#include "rules.h"

/*
 *  (see rule.h and asn1module.h)
*
*/


CRules cRulesG =
{
    4,
    "choiceId",
    "ChoiceId",
    "a",
    "ChoiceUnion",
    TRUE,
    "Print",
    "Enc",
    "Dec",
    "Free",
    {
        {
            BASICTYPE_UNKNOWN,
            C_NO_TYPE,
            NULL,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "unknown",
            NULL,
            NULL,
            NULL,
            NULL,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE
        },
        {
            BASICTYPE_BOOLEAN,
            C_LIB,
            "AsnBool",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            TRUE,
            "NOT_NULL",
            "bool",
            "PrintAsnBool",
            "EncAsnBool",
            "DecAsnBool",
            "FreeAsnBool",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_INTEGER,
            C_LIB,
            "AsnInt",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            TRUE,
            "NOT_NULL",
            "int",
            "PrintAsnInt",
            "EncAsnInt",
            "DecAsnInt",
            "FreeAsnInt",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_BITSTRING,
            C_LIB,
            "AsnBits",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            TRUE,
            FALSE,
            "ASNBITS_PRESENT",
            "bits",
            "PrintAsnBits",
            "EncAsnBits",
            "DecAsnBits",
            "FreeAsnBits",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_OCTETSTRING,
            C_LIB,
            "AsnOcts",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            TRUE,
            FALSE,
            "ASNOCTS_PRESENT",
            "octs",
            "PrintAsnOcts",
            "EncAsnOcts",
            "DecAsnOcts",
            "FreeAsnOcts",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_NULL,
            C_LIB,
            "AsnNull",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            TRUE,
            "NOT_NULL",
            "null",
            "PrintAsnNull",
            "EncAsnNull",
            "DecAsnNull",
            "FreeAsnNull",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_OID,
            C_LIB,
            "AsnOid",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            TRUE,
            FALSE,
            "ASNOID_PRESENT",
            "oid",
            "PrintAsnOid",
            "EncAsnOid",
            "DecAsnOid",
            "FreeAsnOid",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_REAL,
            C_LIB,
            "AsnReal",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            TRUE,
            "NOT_NULL",
            "real",
            "PrintAsnReal",
            "EncAsnReal",
            "DecAsnReal",
            "FreeAsnReal",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_ENUMERATED,
            C_LIB,
            "enum",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            TRUE,
            "NOT_NULL",
            "enum",
            "PrintAsnEnum",
            "EncAsnEnum",
            "DecAsnEnum",
            "FreeAsnEnum",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_SEQUENCE,
            C_STRUCT,
            "struct",
            FALSE,
            TRUE,
            FALSE,
            TRUE,
            TRUE,
            TRUE,
            "NOT_NULL",
            "seq",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_SEQUENCEOF,
            C_LIST,
            "AsnList",
            FALSE,
            TRUE,
            FALSE,
            TRUE,
            TRUE,
            TRUE,
            "NOT_NULL",
            "list",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_SET,
            C_STRUCT,
            "struct",
            FALSE,
            TRUE,
            FALSE,
            TRUE,
            TRUE,
            TRUE,
            "NOT_NULL",
            "set",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_SETOF,
            C_LIST,
            "AsnList",
            FALSE,
            TRUE,
            FALSE,
            TRUE,
            TRUE,
            TRUE,
            "NOT_NULL",
            "list",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_CHOICE,
            C_CHOICE,
            NULL,
            FALSE,
            TRUE,
            FALSE,
            TRUE,
            TRUE,
            TRUE,
            "NOT_NULL",
            "choice",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_SELECTION,
            C_NO_TYPE,
            NULL,
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "selection",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_COMPONENTSOF,
            C_NO_TYPE,
            NULL,
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "compsOf",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_ANY,
            C_ANY,
            "AsnAny",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "any",
            "PrintAsnAny",
            "EncAsnAny",
            "DecAsnAny",
            "FreeAsnAny",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_ANYDEFINEDBY,
            C_ANYDEFINEDBY,
            "AsnAnyDefinedBy",
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "anyDefBy",
            "PrintAsnAnyDefinedBy",
            "EncAsnAnyDefinedBy",
            "DecAsnAnyDefinedBy",
            "FreeAsnAnyDefinedBy",
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_LOCALTYPEREF,
            C_TYPEREF,
            NULL,
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "t",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_IMPORTTYPEREF,
            C_TYPEREF,
            NULL,
            FALSE,
            TRUE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "t",
            NULL,
            NULL,
            NULL,
            NULL,
            TRUE,
            TRUE,
            TRUE,
            TRUE,
            TRUE
        },
        {
            BASICTYPE_MACROTYPE,
            C_NO_TYPE,
            NULL,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "macroType",
            NULL,
            NULL,
            NULL,
            NULL,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE
        },
        {
            BASICTYPE_MACRODEF,
            C_NO_TYPE,
            NULL,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            "NOT_NULL",
            "macroDef",
            NULL,
            NULL,
            NULL,
            NULL,
            FALSE,
            FALSE,
            FALSE,
            FALSE,
            FALSE
        }
    }
};