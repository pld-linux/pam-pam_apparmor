%define		modulename pam_apparmor
Summary:	PAM module to add AppArmor change_hat functionality
Summary(pl.UTF-8):	Moduł PAM dodający funkcjonalność AppArmor change_hat
Name:		pam-%{modulename}
Version:	2.5
Release:	1
Epoch:		1
License:	GPL
Group:		Base
Source0:	http://kernel.org/pub/linux/security/apparmor/AppArmor-%{version}/AppArmor-%{version}.tgz
# Source0-md5:	4a747d1a1f85cb272d55b52c7e8a4a02
URL:		http://apparmor.wiki.kernel.org/
BuildRequires:	libapparmor-devel
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pam_apparmor module provides the means for any PAM applications
that call pam_open_session() to automatically perform an AppArmor
change_hat operation in order to switch to a user-specific security
policy.

%description -l pl.UTF-8
Moduł pam_apparmor daje możliwość każdej aplikacji PAM wywołującej
pam_open_session() automatycznie wykonać operację AppArmor change_hat
w celu przełączenia na specyficzną dla użytkownika politykę
bezpieczeństwa.

%prep
%setup -q -n AppArmor-%{version}

%build
%{__make} -C changehat/pam_apparmor \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -D changehat/pam_apparmor/pam_apparmor.so $RPM_BUILD_ROOT/%{_lib}/security/pam_apparmor.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changehat/pam_apparmor/README
%attr(755,root,root) /%{_lib}/security/pam_apparmor.so
