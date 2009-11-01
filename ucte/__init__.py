#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANDABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------



# <<< imports
# @generated
from google.appengine.ext import db
# >>> imports

#------------------------------------------------------------------------------
#  Properties:
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

NS_PREFIX = "cim"
NS_URI = "http://iec.ch/TC57/2009/CIM-schema-cim14#"

#------------------------------------------------------------------------------
#  "Element" class:
#------------------------------------------------------------------------------

class Element(db.Model):
    
    uri = db.StringProperty()

    # 
    model = db.ReferenceProperty(collection_name="elements")

    # <<< element
    # @generated
    # >>> element


#------------------------------------------------------------------------------
#  "Model" class:
#------------------------------------------------------------------------------

class Model(db.Model):
    
    uri = db.StringProperty()

    # Virtual property. 
    pass #elements

    # <<< model
    # @generated
    # >>> model


#------------------------------------------------------------------------------
#  "IEC61970CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.
    """

    
    # The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.The date of release of the model version.  Of the form 2008-12-22 for example if the date was the twentysecond day of December in 2008.
    date = db.DateProperty()

    # Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments. Version number of the model.   Of the form IEC61970CIM14v01 for example.  For UCTE on 2009-01-15 added the terminal.SequenceNumber  added some clarification of MutualCoupling  For UCTE on 2009-0116 added IdentifiedObject inhereitance to OperationalLimitType class  For UCTE on 2009-01-17 added the TopologicalNode-BaseVoltage association.  For UCTE on 2009-01-27 added the TopologicalNode.equivalent attribute.  For UCTE on 2009-02-04 renamed SvTapStep.tapRatio to SvTapStep.continuousPosition. Multipliicty made optional or SvTapStep.position and SvTapStep.continuousPosition.Please see the profile comments on the IEC61970CIMVersion class for the profile version comments. 
    version = db.StringProperty()

    # <<< iec61970_cimversion
    # @generated
    # >>> iec61970_cimversion




# EOF -------------------------------------------------------------------------
