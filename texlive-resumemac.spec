Name:		texlive-resumemac
Version:	15878
Release:	2
Summary:	Plain TeX macros for resumes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/resumemac
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumemac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumemac.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of macros is provided, together with an file that offers
an example of use.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/resumemac/resumemac.tex
%doc %{_texmfdistdir}/doc/plain/resumemac/README
%doc %{_texmfdistdir}/doc/plain/resumemac/sample_resume.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
