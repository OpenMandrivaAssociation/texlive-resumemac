# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/resumemac
# catalog-date 2008-11-21 01:34:08 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-resumemac
Version:	20180303
Release:	2
Summary:	Plain TeX macros for resumes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/resumemac
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumemac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/resumemac.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081121-2
+ Revision: 755661
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081121-1
+ Revision: 719451
- texlive-resumemac
- texlive-resumemac
- texlive-resumemac
- texlive-resumemac

