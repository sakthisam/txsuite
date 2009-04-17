#! /usr/bin/env python

#
# Copyright (C) 2004  Lorenzo Pallara, lpallara@cineca.it
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#                                  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#                                  
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# transport_stream_sat and transport_stream_cable descriptors by Kovacs Balazs

import string
from dvbobjects.utils import *
from dvbobjects.MPEG.Descriptor import Descriptor

######################################################################                                                                                                                 
class short_event_descriptor(Descriptor):                                                                                                                                              

    descriptor_tag = 0x4D
    
    def bytes(self):
	assert len(self.ISO639_language_code) == 3
	fmt = "!%dsB%dsB%ds" % (
	    len(self.ISO639_language_code),
	    len(self.event_name),
	    len(self.text),
	)
	return pack(fmt,
	    self.ISO639_language_code,
	    len(self.event_name),
	    self.event_name,
	    len(self.text),
	    self.text,
	)

######################################################################
class parental_rating_descriptor(Descriptor):                                                                                                                                              

    descriptor_tag = 0x55
    
    def bytes(self):
	assert len(self.country_code) == 3
	fmt = "!%dsB" % (
	    len(self.country_code),
	)
	return pack(fmt,
	    self.country_code,
	    self.rating,
	)


######################################################################
class teletext_descriptor(Descriptor):

    descriptor_tag = 0x56

    def bytes(self):
	assert len(self.ISO639_language_code) == 3
	fmt = "!%dsBB" % len(self.ISO639_language_code)
	return pack(fmt,
	    self.ISO639_language_code,
	    (self.type << 3) | 
	    (self.magazine_number & 0x1F),
	    self.page_number,
		)

######################################################################
class vbi_data_descriptor_loop_item(DVBobject):

    def pack(self):
            fmt = "!B"
	    return pack(fmt,
		0x3F & 
		((self.field_parity & 0x01) >> 5) | 
		(self.line_offset & 0x1F),    
		)

class vbi_data_descriptor(Descriptor):

    descriptor_tag = 0x45

    def bytes(self):
	data_bytes = string.join(
		    map(lambda x: x.pack(),
		    self.vbi_data_descriptor_loop),
		    "")
		    
	fmt = "!BB%ds" % len(data_bytes)
	return pack(fmt,
	    self.data_service_id,
	    len(data_bytes),
	    data_bytes,
		)

######################################################################
class stream_identifier_descriptor(Descriptor):

    descriptor_tag = 0x52

    def bytes(self):
	fmt = "!B"
	return pack(fmt,
		    self.component_tag,
		)

######################################################################
class data_broadcast_id_descriptor(Descriptor):

    descriptor_tag = 0x66

    def bytes(self):
        FMT = "!H%ds" % len(self.ID_selector_bytes)
        return pack(FMT,         
                    self.data_broadcast_ID,
                    self.ID_selector_bytes,
                    )            
                                 
######################################################################
class application_signalling_descriptor(Descriptor):

    descriptor_tag = 0x6F

    def bytes(self):
        FMT = "!HB"
        return pack(FMT, 
		self.application_type,
		0xE0 | (self.AIT_version & 0x1F),
                )
		    
######################################################################
class network_descriptor(Descriptor):

    descriptor_tag = 0x40

    def bytes(self):
        fmt = "!B%ds" % len(self.network_name)
        return pack(fmt,
                    len(self.network_name),
                    self.network_name,
                    )
		    
######################################################################
class service_descriptor(Descriptor):

    descriptor_tag = 0x48

    def bytes(self):
        fmt = "!BB%dsB%ds" % (len(self.service_provider_name), len(self.service_name))
        return pack(fmt,
		    self.service_type,
		    len(self.service_provider_name),
		    self.service_provider_name,
		    len(self.service_name),
		    self.service_name,
                    )


######################################################################
#class transport_stream_terrestrial_descriptor(Descriptor):

#    descriptor_tag = 0x5a

#    def bytes(self):
#        fmt = "!LBBBL"
#        return pack(fmt,
#                    self.center_frequency,
#		    (self.bandwidth << 5) | 0x1f,
#		    (self.constellation << 6) | (self.hierarchy_information << 3)| (self.code_rate_HP_stream),
#		    (self.code_rate_LP_stream << 6) | (self.guard_interval << 3) | (self.transmission_mode << 2) | (self.other_frequency_flag),
#		    0xffffffff,
#                    )

######################################################################
class transport_stream_sat_descriptor(Descriptor):

    descriptor_tag = 0x43
 
    def bytes(self):
	fmt = "!LHBL"
	return pack(fmt,
		self.frequency,
		self.orbital_position,
		(self.west_east_flag << 7) | (self.polarization << 5) |  self.modulation,
		(self.symbol_rate << 4)| self.FEC_inner,
	)
 
#######################################################################
class transport_stream_cable_descriptor(Descriptor):

    descriptor_tag = 0x44
 
    def bytes(self):
	fmt = "!LHBL"
	return pack(fmt,
	    self.frequency,
	    (self.FEC_outer) | 0xFFF0,
	    (self.modulation),
	    (self.symbol_rate << 4)| (self.FEC_inner),
	)
 		    
######################################################################
class service_descriptor_loop_item(DVBobject):

    def pack(self):
	fmt = "!HB"
	return pack(fmt,
	    self.service_ID,
	    self.service_type,
	)

class service_list_descriptor(Descriptor):

    descriptor_tag = 0x41

    def bytes(self):
        dvb_service_bytes = string.join(
	    map(lambda x: x.pack(),	
                self.dvb_service_descriptor_loop),
            "")								    

        FMT = "!%ds" % len(dvb_service_bytes)
        return pack(FMT,
                    dvb_service_bytes,
                    )

######################################################################
class lcn_service_descriptor_loop_item(DVBobject):

    def pack(self):
	fmt = "!HH"
	return pack(fmt,
	    self.service_ID,
	    ((self.visible_service_flag << 15) | 0x7C00 | self.logical_channel_number),
	)

class logical_channel_descriptor(Descriptor):

    descriptor_tag = 0x83

    def bytes(self):
        lcn_service_bytes = string.join(
	    map(lambda x: x.pack(),	
                self.lcn_service_descriptor_loop),
            "")								    

        FMT = "!%ds" % len(lcn_service_bytes)
        return pack(FMT,
                    lcn_service_bytes,
                    )

######################################################################
class component_descriptor(Descriptor):

    descriptor_tag = 0x50

    def bytes(self):
        fmt = "!BBB%ds%ds" % (
			len(self.ISO_639_language_code),
			len(self.text_char),
			)
        return pack(fmt,
                    0xF0 | (self.stream_content),
                    self.component_type,
		    self.component_tag,
		    self.ISO_639_language_code,
		    self.text_char,
        )

######################################################################
class PDC_descriptor(Descriptor):

    descriptor_tag = 0x69

    def bytes(self):
        fmt = "!BH"
        return pack(fmt,
                    (0xF0) | (self.day >> 1),
		    (self.day << 15) | (self.month << 11) | (self.hour << 6) | (self.minute),
        )
					

#
# Copyright (C) 2004  Andreas Berger, berger@ftw.at
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#                                  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#                                  
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


class ip_mac_platform_name_descriptor(Descriptor):
    
    descriptor_tag = 0x0c
    
    def bytes(self):
    
        fmt = "!3s%ds" % len(self.text_char_bytes)
    
        return pack(fmt,
                    self.ISO_639_language_code,
                    self.text_char_bytes
                    )
    
class ip_mac_platform_provider_name_descriptor(Descriptor):
    
    descriptor_tag = 0x0d
    
    def bytes(self):
    
        fmt = "!3s%ds" % len(self.text_char_bytes)
    
        return pack(fmt,
                    self.ISO_639_language_code,
                    self.text_char_bytes
                    )

class target_serial_number_descriptor(Descriptor):
    
    descriptor_tag = 0x08
    
    def bytes(self):
    
        fmt = "!%ds" % len(serial_data_bytes)
    
        return pack(fmt,
                    self.serial_data_bytes
                    )

class target_smartcard_descriptor(Descriptor):
    
    descriptor_tag = 0x06
    
    def bytes(self):
    
        fmt = "!I%ds" % len(self.private_data_bytes)
    
        return pack(fmt,
                    self.super_CA_system_id,
                    self.private_data_bytes
                    )                    

class target_MAC_address_descriptor(Descriptor):
    
    descriptor_tag = 0x07
    
    def bytes(self):
    
        fmt = "!6s%ds" % len(self.mac_addr_bytes)
    
        return pack(fmt,
                    self.mac_addr_mask,
                    self.mac_addr_bytes
                    ) 

class target_MAC_address_range_descriptor(Descriptor):
    
    descriptor_tag = 0x0e
    
    def bytes(self):
    
        fmt = "!6s%ds" % len(self.mac_addr_bytes)
    
        return pack(fmt,
                    self.mac_addr_mask,
                    self.mac_addr_bytes
                    )   

class target_IP_address_descriptor(Descriptor):
    
    descriptor_tag = 0x09
    
    def bytes(self):
    
        fmt = "!I%dI" % len(self.IPv4_addr_bytes)
    
        return pack(fmt,
                    self.IPv4_addr_mask,
                    self.IPv4_addr_bytes
                    )   
 
class target_IP_slash_descriptor(Descriptor):
    
    descriptor_tag = 0x0f
    
    def bytes(self):
    
        fmt = "!4BB"
    
        return pack(fmt,
                    self.IPv4_addr[0],
                    self.IPv4_addr[1],
                    self.IPv4_addr[2],
                    self.IPv4_addr[3],
                    self.IPv4_slash_mask
                    )   

class target_IP_source_slash_descriptor(Descriptor):
    
    descriptor_tag = 0x10
    
    def bytes(self):
    
        fmt = "!%ds" % len(self.IPv4_source_dest_bytes)
    
        return pack(fmt,
                    self.IPv4_source_dest_bytes
                    )   

class target_IPv6_address_descriptor(Descriptor):
    
    descriptor_tag = 0x0a
    
    def bytes(self):
    
        fmt = "!7s%ds" % len(self.IPv6_address_bytes)
    
        return pack(fmt,
                    self.IPv6_address_mask,
                    self.IPv6_address_bytes
                    )   

class target_IPv6_slash_descriptor(Descriptor):
    
    descriptor_tag = 0x11
    
    def bytes(self):
    
        fmt = "!%ds" % len(self.IPv6_bytes)
    
        return pack(fmt,
                    self.IPv6_bytes
                    )   

class target_IPv6_source_slash_descriptor(Descriptor):
    
    descriptor_tag = 0x12
    
    def bytes(self):
    
        fmt = "!%ds" % len(self.IPv6_source_dest_bytes)
    
        return pack(fmt,
                    self.IPv6_source_dest_bytes
                    )   

class ip_mac_stream_location_descriptor(Descriptor):
    
    descriptor_tag = 0x13
    
    def bytes(self):
    
        fmt = "!HHHHB"
    
        return pack(fmt,
                    self.network_id,
                    self.original_network_id,
                    self.transport_stream_id,
                    self.service_id,
                    self.component_tag
                    )

class isp_access_mode_descriptor(Descriptor):
    
    descriptor_tag = 0x14
    
    def bytes(self):
    
        fmt = "!B"
    
        return pack(fmt,
                    self.access_mode
                    )

class telephone_descriptor(Descriptor):
    
    descriptor_tag = 0x57
    
    def bytes(self):
    
        fmt = "!BBBB%ds%ds%ds%ds%ds" % (len(country_prefix_bytes), len(international_area_code_bytes), len(operator_code_bytes), len(national_area_code_bytes), len(core_number_bytes))
    
        return pack(fmt,
                    (0x03 << 7) & 0xC0 | (self.foreign_availability << 5) & 0x20 | self.connection_type & 0x1F,
                    (0x01 << 7) & 0x80 | (self.country_prefix_length << 5) & 0x60 | (self.international_area_code << 4) & 0x1C | self.operator_code_length & 0x07,
                    (0x01 << 7) & 0x80 | (self.national_area_code_length << 4) & 0x70 | self.core_number_length & 0x0F, 
                    country_prefix_bytes,
                    international_area_code_bytes,
                    operator_code_bytes,
                    national_area_code_bytes,
                    core_number_bytes
                    )
  
class private_data_specifier_descriptor(Descriptor):
    
    descriptor_tag = 0x5f
    
    def bytes(self):
    
        fmt = "!I"
    
        return pack(fmt,
                    self.private_data_specifier
                    )

class time_slice_fec_identifier_descriptor(Descriptor):
    
    descriptor_tag = 0x77

    def bytes(self):

    	time_slice_fec_id = 0x00;

        fmt = "!BBB"

        return pack(fmt,
                    (self.time_slicing << 7) & 0x80 | (self.mpe_fec << 5) & 0x60 | (0x03 << 4) & 0x18 | self.frame_size & 0x07,
                    self.max_burst_duration,
                    (self.max_average_rate << 4) & 0xF0 | time_slice_fec_id & 0x0F,
                    )

# FIXME: move this class to another file, it's no descriptor
class platform_id_data2(DVBobject):
  
  def pack(self):
	fmt = "!BBBBB"

	return pack(fmt,
		    (self.platform_id >> 16) & 0xFF,
		    (self.platform_id >> 8) & 0xFF,
		    self.platform_id  & 0xFF,
		    self.action_type & 0xFF,
		    (0x03 << 6) & 0xC0 | (0x00 << 5) & 0x20 | 0x01 & 0x1F
		    )
    

# FIXME: move this class to another file, it's no descriptor
class ip_mac_notification_info(DVBobject):

  def pack(self):
	  
    # pack platform id data loop
    pid_bytes = string.join(
      map(lambda x: x.pack(),
	self.platform_id_data_loop),
      "")

    platform_id_data_length = len(pid_bytes);

    fmt = "!B%ds%ds" % (platform_id_data_length, len(self.private_data_bytes))

    return pack(fmt,
		platform_id_data_length,
		pid_bytes,
		self.private_data_bytes
		)

# FIXME: move this class to another file, it's no descriptor
class platform_name(DVBobject):
  
  def pack(self):
	platform_name_length = len(self.text_char_bytes)

	fmt = "!3sB%ds" % platform_name_length

	return pack(fmt,
		    self.ISO_639_language_code,
		    platform_name_length,
		    self.text_char_bytes
		    )

# FIXME: move this class to another file, it's no descriptor
class platform_id_data(DVBobject):

  def pack(self):
	  
	pn_bytes = string.join(
	  map(lambda x: x.pack(),
	    self.platform_name_loop),
          "")

	platform_name_loop_length = len(pn_bytes)

	fmt = "!BBBB%ds" % platform_name_loop_length

	return pack(fmt,
		    (self.platform_id >> 16) & 0xFF,
		    (self.platform_id >> 8) & 0xFF,
		    self.platform_id  & 0xFF,
		    platform_name_loop_length,
		    pn_bytes
		    )
  
class linkage_descriptor(Descriptor):
    
    descriptor_tag = 0x4A;

    def bytes(self):

	if (self.linkage_type == 0x0B):
        
	  # pack platform id data loop
	  pid_bytes = string.join(
          map(lambda x: x.pack(),
	    self.platform_id_data_loop),
          "")

	  platform_id_data_length = len(pid_bytes);

	  fmt = "!BBBBBBBB%ds%ds" % (platform_id_data_length, len(self.private_data_bytes))

	  return pack(fmt,
		    (self.transport_stream_id >> 8) & 0xFF,
		    self.transport_stream_id & 0xFF,
		    (self.original_network_id >> 8) & 0xFF,
		    self.original_network_id & 0xFF,
		    (self.service_id >> 8) & 0xFF,
		    self.service_id & 0xFF,
		    self.linkage_type,
		    platform_id_data_length,
		    pid_bytes,
		    self.private_data_bytes
		    )
	else:
	  fmt = "!BBBBBBB%ds"

	  # we care only for linkage_type = 0x0B, other linkage descriptors
	  # have to be implemented according to ETSI EN 300 468 standard

	  return pack(fmt,
		    (self.transport_stream_id >> 8) & 0xFF,
		    self.transport_stream_id & 0xFF,
		    (self.original_network_id >> 8) & 0xFF,
		    self.original_network_id & 0xFF,
		    (self.service_id >> 8) & 0xFF,
		    self.service_id & 0xFF,
		    self.linkage_type,
		    private_data_bytes
		    )

class terrestrial_delivery_system_descriptor(Descriptor):

    descriptor_tag = 0x5a

    def bytes(self):
        fmt = "!LBBBL"
	priority = 1
	timeslice_ind = 1
	mpe_fec_ind = 1
        return pack(fmt,
                    self.center_frequency & 0xFFFFFFFF,
		    (self.bandwidth << 5) & 0xE0 | (self.priority << 4) & 0x10 | (self.timeslice_ind << 3) & 0x08 |
		    (self.mpe_fec_ind << 2) & 0x04 | 0x03,
		    (self.constellation << 6) | (self.hierarchy_information << 3)| (self.code_rate_HP_stream),
		    (self.code_rate_LP_stream << 5) | (self.guard_interval << 3) | (self.transmission_mode << 1) | (self.other_frequency_flag),
		    0xffffffff,
                    )