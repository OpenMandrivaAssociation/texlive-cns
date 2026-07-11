%global tl_name cns
%global tl_revision 45677

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2.0
Release:	%{tl_revision}.1
Summary:	Chinese/Japanese/Korean bitmap fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/CJK
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cns.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cns.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fonts to go with the cjk macro package for Chinese, Japanese and Korean
with LaTeX2e. The package aims to supersede HLaTeX fonts bundle.

