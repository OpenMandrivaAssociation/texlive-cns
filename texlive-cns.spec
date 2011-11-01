Name:		texlive-cns
Version:	20111101
Release:	1
Summary:	TeXLive cns package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cns.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cns.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive cns package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/cns/4040w0.bin
%{_texmfdistdir}/fonts/misc/cns/4040w1.bin
%{_texmfdistdir}/fonts/misc/cns/4040w2.bin
%{_texmfdistdir}/fonts/misc/cns/4040w3.bin
%{_texmfdistdir}/fonts/misc/cns/4040w4.bin
%{_texmfdistdir}/fonts/misc/cns/4040w5.bin
%{_texmfdistdir}/fonts/misc/cns/4040w6.bin
%{_texmfdistdir}/fonts/misc/cns/4040w7.bin
%{_texmfdistdir}/fonts/misc/cns/cns40-1.hbf
%{_texmfdistdir}/fonts/misc/cns/cns40-2.hbf
%{_texmfdistdir}/fonts/misc/cns/cns40-3.hbf
%{_texmfdistdir}/fonts/misc/cns/cns40-4.hbf
%{_texmfdistdir}/fonts/misc/cns/cns40-5.hbf
%{_texmfdistdir}/fonts/misc/cns/cns40-6.hbf
%{_texmfdistdir}/fonts/misc/cns/cns40-7.hbf
%{_texmfdistdir}/fonts/misc/cns/cns40-b5.hbf
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1226.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1227.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1228.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1229.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1230.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1231.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1232.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1233.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1234.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1235.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1236.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1237.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1238.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1239.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1240.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1241.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1242.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1243.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1244.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1245.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1246.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1247.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1248.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1249.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1250.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1251.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1252.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1253.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1254.tfm
%{_texmfdistdir}/fonts/tfm/cns/c0so12/c0so1255.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1226.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1227.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1228.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1229.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1230.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1231.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1232.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1233.tfm
%{_texmfdistdir}/fonts/tfm/cns/c1so12/c1so1234.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1226.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1227.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1228.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1229.tfm
%{_texmfdistdir}/fonts/tfm/cns/c2so12/c2so1230.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c3so12/c3so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1226.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1227.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1228.tfm
%{_texmfdistdir}/fonts/tfm/cns/c4so12/c4so1229.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1226.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1227.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1228.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1229.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1230.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1231.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1232.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1233.tfm
%{_texmfdistdir}/fonts/tfm/cns/c5so12/c5so1234.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c6so12/c6so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1201.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1202.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1203.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1204.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1205.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1206.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1207.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1208.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1209.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1210.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1211.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1212.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1213.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1214.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1215.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1216.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1217.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1218.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1219.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1220.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1221.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1222.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1223.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1224.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1225.tfm
%{_texmfdistdir}/fonts/tfm/cns/c7so12/c7so1226.tfm
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-1/README
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-2/README
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-3/README
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-4/README
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-5/README
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-6/README
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-7/README
%doc %{_texmfdistdir}/doc/fonts/cns/cns40-b5/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
