%global tl_name testidx
%global tl_revision 60966

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Dummy text for testing index styles and indexing applications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/testidx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/testidx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/testidx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/testidx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package that provides a command to produce dummy text
interspersed with \index commands to test an index style or indexing
application. The dummy text is mostly in English, but includes extended
Latin characters provided either through LaTeX accent commands or
directly with UTF-8 characters, depending on the setup, to allow for
testing extended Latin alphabets. The supplementary package testidx-
glossaries.sty uses the indexing interface provided by the glossaries
package.

