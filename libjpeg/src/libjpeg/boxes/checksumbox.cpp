/*************************************************************************

    This project implements a complete(!) JPEG (Recommendation ITU-T
    T.81 | ISO/IEC 10918-1) codec, plus a library that can be used to
    encode and decode JPEG streams. 
    It also implements ISO/IEC 18477 aka JPEG XT which is an extension
    towards intermediate, high-dynamic-range lossy and lossless coding
    of JPEG. In specific, it supports ISO/IEC 18477-3/-6/-7/-8 encoding.

    Note that only Profiles C and D of ISO/IEC 18477-7 are supported
    here. Check the JPEG XT reference software for a full implementation
    of ISO/IEC 18477-7.

    Copyright (C) 2012-2018 Thomas Richter, University of Stuttgart and
    Accusoft. (C) 2019-2020 Thomas Richter, Fraunhofer IIS.

    This program is available under two licenses, GPLv3 and the ITU
    Software licence Annex A Option 2, RAND conditions.

    For the full text of the GPU license option, see README.license.gpl.
    For the full text of the ITU license option, see README.license.itu.
    
    You may freely select between these two options.

    For the GPL option, please note the following:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

*************************************************************************/
/*
** This class keeps a simple checksum over the data in the legacy codestream
** thus enabling decoders to check whether the data has been tampered with.
**
** $Id: checksumbox.cpp,v 1.4 2014/09/30 08:33:14 thor Exp $
**
*/

/// Includes
#include "boxes/checksumbox.hpp"
#include "io/bytestream.hpp"
#include "io/memorystream.hpp"
#include "tools/checksum.hpp"
///

/// ChecksumBox::ParseBoxContent
// Second level parsing stage: This is called from the first level
// parser as soon as the data is complete. Must be implemented
// by the concrete box. Returns true in case the contents is
// parsed and the stream can go away.
bool ChecksumBox::ParseBoxContent(class ByteStream *stream,UQUAD boxsize)
{
  LONG pack1,pack2;
  
  if (boxsize != 4)
    JPG_THROW(MALFORMED_STREAM,"ChecksumBox::ParseBoxContent",
              "Malformed JPEG stream, the checksum box size is invalid");
  
  pack1 = stream->GetWord();
  pack2 = stream->GetWord();
  
  m_ulCheck = ULONG(pack1 << 16) | ULONG(pack2);

  return true;
}
///

/// ChecksumBox::CreateBoxContent
// Second level creation stage: Write the box content into a temporary stream
// from which the application markers can be created.
// Returns whether the box content is already complete and the stream
// can go away.
bool ChecksumBox::CreateBoxContent(class MemoryStream *target)
{
  target->PutWord(m_ulCheck >> 16);
  target->PutWord(m_ulCheck);

  return true;
}
///

/// ChecksumBox::InstallChecksum
// Install the value from the checksum into the checksum box.
void ChecksumBox::InstallChecksum(const class Checksum *check)
{
  m_ulCheck = check->ValueOf();
}
///

  
  
