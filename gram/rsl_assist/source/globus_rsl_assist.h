/*
 * globus_rsl_assist.h
 *
 * Description:
 *
 *   This header contains the interface prototypes for the rsl_assist library.
 *   
 * CVS Information:
 *
 * $Source$
 * $Date$
 * $Revision$
 * $Author$
 */
#ifndef _GLOBUS_RSL_ASSIST_INCLUDE_GLOBUS_RSL_ASSIST_H_
#define _GLOBUS_RSL_ASSIST_INCLUDE_GLOBUS_RSL_ASSIST_H_

#ifndef EXTERN_C_BEGIN
#ifdef __cplusplus
#define EXTERN_C_BEGIN extern "C" {
#define EXTERN_C_END }
#else
#define EXTERN_C_BEGIN
#define EXTERN_C_END
#endif
#endif

#include "globus_common.h"
#include "globus_rsl.h"


/*
 * Function: globus_rsl_assist_replace_manager_name()
 *
 * Uses the Globus RSL library and the UMich LDAP
 * library to modify an RSL specification, changing instances of
 *
 * resourceManagerName=x
 *
 * with
 *
 * resourceManagerContact=y
 *
 * where y is obtained by querying the MDS ldap server, searching
 * for an object which matches the following filter
 *
 *   (&(objectclass=GlobusResourceManager)(cn=x))
 *
 * and extracting the contact value for that object.
 * 
 * Parameters: 
 *     rsl - Pointer to the RSL structure in which you want to
 *           replace the manager Name by its Contact.
 *
 *     NOTE: The RSL MUST have been created using globus_rsl_parse, because
 *     the rsl might be reallocated by this function !! (required when
 *     the rsl is only a simple relation equal : resourceManagerName=x
 *
 * Returns:
 *     Pointer to the new RSL (Might be equal to the original one) or
 *     GLOBUS_NULL in case of failure
 *     
 */
globus_rsl_t *
globus_rsl_assist_replace_manager_name(globus_rsl_t * rsl);


#endif


