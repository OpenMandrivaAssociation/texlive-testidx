Name:		texlive-testidx
Version:	60966
Release:	1
Summary:	Dummy text for testing index styles and indexing applications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/testidx
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/testidx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/testidx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/testidx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package that provides a command to produce
dummy text interspersed with \index commands to test an index
style or indexing application. The dummy text is mostly in
English, but includes extended Latin characters provided either
through LaTeX accent commands or directly with UTF-8
characters, depending on the setup, to allow for testing
extended Latin alphabets. The supplementary package
testidx-glossaries.sty uses the indexing interface provided by
the glossaries package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/testidx
%{_texmfdistdir}/tex/latex/testidx
%{_texmfdistdir}/bibtex/bib/testidx
%doc %{_texmfdistdir}/doc/latex/testidx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
