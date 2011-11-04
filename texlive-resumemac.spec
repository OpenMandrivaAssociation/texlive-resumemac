# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/resumemac
# catalog-date 2008-11-21 01:34:08 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-resumemac
Version:	20081121
Release:	1
Summary:	Plain TeX macros for resumes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/resumemac
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumemac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumemac.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A set of macros is provided, together with an file that offers
an example of use.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/resumemac/resumemac.tex
%doc %{_texmfdistdir}/doc/plain/resumemac/README
%doc %{_texmfdistdir}/doc/plain/resumemac/sample_resume.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
