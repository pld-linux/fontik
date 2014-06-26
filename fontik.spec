%define	subver	5dbbc513
%define	rel		1
Summary:	A Configuration Tool for Font-wise, User-set Fontconfig Rules
Name:		fontik
Version:	0.6.1
Release:	0.%{rel}.%{subver}
License:	GPL v3
Group:		X11/Applications
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone git://gitorious.org/fontik/fontik.git
#  cd fontik
#  export subver=5dbbc513
#  git archive --format tar --prefix fontik-${subver}/ ${subver} |\
#      gzip -c > ../fontik-${subver}.tar.gz
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/fontik/%{name}-%{subver}.tar.gz/3ffed0689ff0a5c81bb53135aac38074/fontik-%{subver}.tar.gz
# Source0-md5:	3ffed0689ff0a5c81bb53135aac38074
Source1:	%{name}.desktop
Patch0:		%{name}-valac-save-temps.patch
Patch1:		%{name}-gee-0.8.patch
URL:		http://suruma.freeflux.net/blog/archive/2009/10/14/fontik-a-font-configuration-gui.html
BuildRequires:	desktop-file-utils
BuildRequires:	fontconfig-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgee-devel
BuildRequires:	libxml2-devel
BuildRequires:	vala
BuildRequires:	vala-libgee
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fontik is basically intended to tweak and configure some properties of
fonts. These settings are usually set system-wide while installing the
fonts. The power of fontconfig is thus limited when it comes to the
user.

%prep
%setup -q -n %{name}-%{subver}
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	PROGRAM_LIBEXEC_DIR=%{_libexecdir} \
	DESTDIR=$RPM_BUILD_ROOT

# drop pointless wrapper, use bin directly
mv $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}/fontik

desktop-file-install --dir=$RPM_BUILD_ROOT%{_desktopdir} %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/fontik
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
